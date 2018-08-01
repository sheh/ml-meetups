import time

import cv2
import base64
import boto3
from glob import glob


client = boto3.client('rekognition')


_emotion_name_encode = {
    'ANGRY': 0,
    'DISGUSTED': 1,
    # fear
    'HAPPY': 3,
    'SAD': 4,
    'SURPRISED': 5,
    'CALM': 6,
    'CONFUSED': 7,
}


def aws_face_attributes(img_path):
    fd = open(img_path, mode='rb')
    b = fd.read()
    fd.close()
    faces = client.detect_faces(Image={'Bytes': b}, Attributes=['ALL'])
    if faces:
        f = faces['FaceDetails'][0]
        emo_d = sorted(f["Emotions"], key=lambda x: x["Confidence"], reverse=True)[0]

        return {
            'gender': 0 if f["Gender"]["Value"] == 'Male' else 1,
            'age': range(f["AgeRange"]["Low"], f["AgeRange"]["High"] + 1),
            'emotion': _emotion_name_encode[emo_d['Type']],
        }

