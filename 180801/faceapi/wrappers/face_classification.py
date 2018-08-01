import sys

import cv2
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import dlib

# from utils.datasets import get_labels
# from utils.inference import detect_faces
# from utils.inference import draw_text
# from utils.inference import draw_bounding_box
# from utils.inference import apply_offsets
# from utils.inference import load_detection_model
# from utils.inference import load_image
# from utils.preprocessor import preprocess_input


def get_labels(dataset_name):
    return {0:'angry',1:'disgust',2:'fear',3:'happy',
            4:'sad',5:'surprise',6:'neutral'}


def load_image(image_path, grayscale=False, target_size=None):
    pil_image = image.load_img(image_path, grayscale, target_size)
    return image.img_to_array(pil_image)


def load_detection_model(model_path):
    detection_model = cv2.CascadeClassifier(model_path)
    return detection_model


def detect_faces(detection_model, gray_image_array):
    return detection_model.detectMultiScale(gray_image_array, 1.3, 5)


def apply_offsets(face_coordinates, offsets):
    x, y, width, height = face_coordinates
    x_off, y_off = offsets
    return (max([0, x - x_off]), x + width + x_off, max([0, y - y_off]), y + height + y_off)


def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x

# parameters for loading data and images
detection_model_path = './data/detection_models/haarcascade_frontalface_default.xml'
emotion_model_path = './data/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
gender_model_path = './data/gender_models/simple_CNN.81-0.96.hdf5'
emotion_labels = get_labels('fer2013')
gender_labels = get_labels('imdb')
font = cv2.FONT_HERSHEY_SIMPLEX

# hyper-parameters for bounding boxes shape
gender_offsets = (30, 60)
gender_offsets = (10, 10)
emotion_offsets = (20, 40)
emotion_offsets = (0, 0)

# loading models
face_detection = load_detection_model(detection_model_path)
dlib_face_detection = dlib.get_frontal_face_detector()
emotion_classifier = load_model(emotion_model_path, compile=False)
gender_classifier = load_model(gender_model_path, compile=False)

# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]
gender_target_size = gender_classifier.input_shape[1:3]


def fc_face_attributes(img_path):
    # loading images
    rgb_image = load_image(img_path, grayscale=False)
    gray_image = load_image(img_path, grayscale=True)
    gray_image = np.squeeze(gray_image)
    gray_image = gray_image.astype('uint8')

    faces = detect_faces(face_detection, gray_image)
    img_dlib = dlib.load_rgb_image(img_path)
    dlib_faces = dlib_face_detection(img_dlib, 0)
    gender_label_arg = emotion_label_arg = None
    for dlib_rect in dlib_faces:
        # x, y, width, height = face_coordinates
        face_coordinates = (dlib_rect.left(), dlib_rect.top(), dlib_rect.width(), dlib_rect.height())
        x1, x2, y1, y2 = apply_offsets(face_coordinates, gender_offsets)
        rgb_face = rgb_image[y1:y2, x1:x2]

        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
        gray_face = gray_image[y1:y2, x1:x2]

        try:
            rgb_face = cv2.resize(rgb_face, (gender_target_size))
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue

        rgb_face = preprocess_input(rgb_face, False)
        rgb_face = np.expand_dims(rgb_face, 0)
        gender_prediction = gender_classifier.predict(rgb_face)
        gender_label_arg = np.argmax(gender_prediction)
        gender_text = gender_labels[gender_label_arg]

        gray_face = preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
        emotion_text = emotion_labels[emotion_label_arg]

    return {
        'gender': gender_label_arg,
        'age': None,
        'emotion': emotion_label_arg,
    }
        # if gender_text == gender_labels[0]:
        #     color = (0, 0, 255)
        # else:
        #     color = (255, 0, 0)

        # draw_bounding_box(face_coordinates, rgb_image, color)
        # draw_text(face_coordinates, rgb_image, gender_text, color, 0, -20, 1, 2)
        # draw_text(face_coordinates, rgb_image, emotion_text, color, 0, -50, 1, 2)

    # bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    # cv2.imwrite('../images/predicted_test_image.png', bgr_image)