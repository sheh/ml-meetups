import cv2
from glob import glob
import time



 ''  # Replace with a valid subscription key (keeping the quotes in place).


def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))


for file_name in glob("images/frame*.jpg"):
    faces = CF.face.detect(file_name, attributes="age,gender,emotion")
    #faces = [{'faceId': '4018b199-fc30-42f4-84d6-fd965ef76552', 'faceRectangle': {'top': 105, 'left': 153, 'width': 257, 'height': 254}, 'faceAttributes': {'gender': 'male', 'age': 27.0, 'emotion': {'anger': 0.0, 'contempt': 0.007, 'disgust': 0.001, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.086, 'sadness': 0.905, 'surprise': 0.0}}}]
    img = cv2.imread(file_name)
    for f in faces:
        p1, p2 = getRectangle(f)
        cv2.rectangle(img, p1, p2, (0, 255, 0), 2)
        attr = f['faceAttributes']

        attr_text = [
            f'gender: {attr["gender"]}',
            f'age: {attr["age"]}',
            f'emotion: {",".join(list(map(lambda x: x[0], filter(lambda x: x[1] > 0.5, attr["emotion"].items()))))}',
        ]

        y0, dy = 20, 18
        for i, line in enumerate(attr_text):
            y = y0 + i * dy
            cv2.putText(img, line, (10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 1)

    cv2.imshow('image', img)
    cv2.imwrite(f'ms/{file_name.split("/")[-1].split(".")[0]}.png', img)
    cv2.waitKey(3000)
    print(faces)

cv2.destroyAllWindows()


# [{'faceId': '25129799-ada1-4a99-b0f1-4fc15e406f86',
#   'faceRectangle': {'top': 124, 'left': 459, 'width': 227, 'height': 227},
#   'faceAttributes': {'gender': 'female', 'age': 24.0, 'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}}}]