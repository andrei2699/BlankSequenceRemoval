import cv2


def capture_live_video_condition(cap):
    return True


def capture_video_from_file_condition(cap):
    return cap.isOpened()


def capture_video(process_frame, set_frame_size, file_path=None):
    if file_path is None:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(file_path)

    set_frame_size((cap.get(3), cap.get(4)))

    condition = capture_live_video_condition if file_path is None else capture_video_from_file_condition
    last_frame = None

    while condition(cap):
        ret, frame = cap.read()

        if not ret:
            print('read failed')
            break

        cv2.imshow('original', frame)

        process_frame(last_frame, frame)

        last_frame = frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
