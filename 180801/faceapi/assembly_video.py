import re
from glob import glob

import cv2


FPS = 1

PROVIDER = 'aws'


if __name__ == '__main__':
    cap = cv2.VideoCapture('origin_emotions.mp4')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{PROVIDER}_emotions.mp4', fourcc, FPS, (int(width), int(height)))


    frames = []
    for file_name in glob(f"{PROVIDER}/frame*.png"):
        frame_n = re.findall("frame(\d+).png", file_name)
        if frame_n:
            frames.append((int(frame_n[0]), file_name))

    for _, img_path in sorted(frames, key=lambda x: x[0]):
        img = cv2.imread(img_path)
        cv2.imshow(img_path, img)
        out.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
