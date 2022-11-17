import cv2


def capture_video_from_file(process_frame, file_path, set_frame_size):
    cap = cv2.VideoCapture(file_path)

    set_frame_size((cap.get(3), cap.get(4)))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print('read failed')
            continue

        frame = process_frame(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
