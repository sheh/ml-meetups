import csv
import io
import os
import pickle
import sys
import cv2
import time
import tempfile
import numpy as np

from wrappers.face_classification import fc_face_attributes
from wrappers.ms import ms_face_attributes

TEST_SIZE = 1000
HISTORY_FILE = 'fre2013_test.pickle'

if __name__ == '__main__':

    i = predicted = 0

    if not os.path.exists(HISTORY_FILE):
        history = []
    else:
        history = pickle.load(open(HISTORY_FILE, 'rb'))

    for row in csv.DictReader(open('data/fer2013.csv')):
        if row['Usage'] != 'PublicTest':
            continue
        i += 1
        if i >= TEST_SIZE:
            break
        if len(history) >= i:
            predicted += history[i-1]
        else:
            img_file = io.BytesIO(bytearray(map(int, row['pixels'].strip().split(' '))))
            tmp_img_path = os.path.join(tempfile.gettempdir(), 'afacefer2013.png')
            image = np.asarray(row['pixels'].strip().split(' '), dtype=np.uint8).reshape((48, 48, 1))
            cv2.imwrite(tmp_img_path, image)
            # ret1 = fc_face_attributes(tmp_img_path)
            ret2 = ms_face_attributes(tmp_img_path)
            print('ms', ret2)
            if ret2 and int(row['emotion']) == ret2['emotion']:
                predicted += 1
                history.append(1)
            else:
                history.append(0)
            pickle.dump(history, open(HISTORY_FILE, 'wb'))
            time.sleep(5)

        print(f'{predicted/i:.0%} ({i})')
        # cv2.imshow('img', image)
        # cv2.waitKey(0)
        #print('fc', ret1)

        #
        #
        # for i in range(48):
        #     for j in range(48):
        #         px = int(pxs[i*48 + j])
        #         image[i][j] = px
        # print(type(image), image.shape, image)
        # #img = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('img', image)
        # cv2.imwrite('test.png', image)
        # cv2.waitKey(0)
        # print(row)
        # break
