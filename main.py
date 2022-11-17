import cv2
import numpy as np

from capture_video import capture_video
from draw_trackbars import draw_trackbars

output_file = 'output.mp4'

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (0, 0))

# parameters threshold
pixel_count = 0
frame_skip = 0

frame_skip_counter = 0


def adjust_pixel_count(value):
    global pixel_count
    pixel_count = value


def adjust_frame_skip(value):
    global frame_skip
    frame_skip = value


def set_frame_size(frame_size):
    global out
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (int(frame_size[0]), int(frame_size[1])))


def process_frame(last_frame, current_frame):
    global out
    global pixel_count
    global frame_skip
    global frame_skip_counter

    if last_frame is None:
        return current_frame

    if frame_skip_counter < frame_skip:
        frame_skip_counter += 1
        return current_frame

    frame_skip_counter = 0

    diff = np.array(cv2.absdiff(last_frame, current_frame))

    diff_count = np.count_nonzero(diff)

    is_blank = False
    if diff_count < pixel_count:
        is_blank = True

    frame = current_frame

    if is_blank:
        cv2.line(frame, (0, 0), (current_frame.shape[1], current_frame.shape[0]), (0, 0, 255), 5)
        cv2.line(frame, (0, current_frame.shape[0]), (current_frame.shape[1], 0), (0, 0, 255), 5)
    else:
        pass
        # out.write(current_frame)

    return frame


def main():
    draw_trackbars(adjust_pixel_count, adjust_frame_skip)

    # noisy_video_path = 'D:/Videos/Music Events Application/metallica-master-of-puppets-live.mp4'
    less_noisy_video_path = 'D:/Videos/Music Events Application/alinacraciunmp4.mp4'

    capture_video(process_frame, set_frame_size)

    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
