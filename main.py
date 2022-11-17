import cv2

from capture_live import capture_live_video

output_file = 'output.mp4'

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (0, 0))


def set_frame_size(frame_size):
    global out
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (int(frame_size[0]), int(frame_size[1])))


def process_frame(frame):
    frame = cv2.flip(frame, 0)

    out.write(frame)

    return frame


def main():
    capture_live_video(process_frame, set_frame_size)

    # noisy_video_path = 'D:/Videos/Music Events Application/metallica-master-of-puppets-live.mp4'
    less_noisy_video_path = 'D:/Videos/Music Events Application/alinacraciunmp4.mp4'
    # capture_video_from_file(process_frame, less_noisy_video_path, set_frame_size)

    out.release()


if __name__ == '__main__':
    main()
