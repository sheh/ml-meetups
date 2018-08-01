import sys
import time
from glob import glob

from wrappers.aws import aws_face_attributes
from wrappers.face_classification import fc_face_attributes
from wrappers.ms import ms_face_attributes
import cv2


convert_get_labels = {
        0: 1,  # angry
        1: 1,  # disgust
        2: 1,  # fear
        3: 0,  # happy
        4: 1,  # sad
        5: 0,  # surprise
        6: 0,  # neutral
        7: 1,  # CONFUSED
    }


def test_class(predic_func, glob_path, class_id):
    i = predicted = 0
    for i, f in enumerate(glob(glob_path)):
        # if f != 'data/0/frame1564.jpg':
        #     continue
        # img = cv2.imread(f)
        # cv2.imshow(f, img)
        # cv2.waitKey(0)
        ret = predic_func(f)
        if ret and ret['emotion'] is not None and convert_get_labels[ret['emotion']] == class_id:
            predicted += 1
        print(f, f'{predicted/(i+1):0.1%}', ret)
    return predicted, i + 1


def test_predictor(predictor_fn):
    pred0, n0 = test_class(predictor_fn, 'data/0/*.jpg', 0)
    pred1, n1 = test_class(predictor_fn, 'data/1/*.jpg', 1)
    print(f'Final result {predictor_fn.__name__}: {(pred0+pred1)/(n0+n1):0.1%}')


def ms_face_attributes_with_pause(f):
    ret = ms_face_attributes(f)
    time.sleep(3)
    return ret


def aws_face_attributes_with_pause(f):
    ret = aws_face_attributes(f)
    time.sleep(3)
    return ret


if __name__ == '__main__':
    test_name = sys.argv[1]
    if test_name == 'ms':
        test_predictor(ms_face_attributes_with_pause)
    elif test_name == 'fc':
        test_predictor(fc_face_attributes)
    elif test_name == 'aws':
        test_predictor(aws_face_attributes_with_pause)
