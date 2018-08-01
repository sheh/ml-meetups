import cv2

FRAME_N = 200


if __name__ == '__main__':
    cap = cv2.VideoCapture('emotions.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames_n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    take_each = frames_n // FRAME_N
    print(f'Video FPS: {fps}, frames_n {frames_n}, take_each {take_each} frame')

    i = 0
    while cap.isOpened():
        i += 1
        success, frame = cap.read()
        if not success:
            break

        if i % take_each == 0:
            cv2.imwrite(f"imgs/frame{i}.jpg", frame)

        # cv2.imshow('frame', frame)
        #
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cap.release()
    cv2.destroyAllWindows()
