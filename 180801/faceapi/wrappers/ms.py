import os

import cognitive_face as CF


API_KEY = os.environ['MS_API_KEY']

CF.Key.set(API_KEY)

BASE_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


_emotion_name_encode = {
        'angry': 0,
        'anger': 0,
        'contempt': 0,
        'disgust': 1,
        'fear': 2,
        'happy': 3,
        'happiness': 3,
        'sad': 4,
        'sadness': 4,
        'surprise': 5,
        'neutral': 6,
}


def ms_face_attributes(img_path):
    faces = CF.face.detect(img_path, attributes="age,gender,emotion")
    if faces:
        face = faces[0]
        attr = face['faceAttributes']
        emotions = map(lambda x: _emotion_name_encode[x[0]], sorted(attr["emotion"].items(), key=lambda x: x[1], reverse=True))
        return {
            'gender': 0 if attr['gender'] == 'male' else 1,
            'age': range(int(attr["age"]), int(attr["age"])),
            'emotion': next(emotions),
        }
