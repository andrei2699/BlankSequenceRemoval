import cv2

from capture_video import capture_video
from draw_trackbars import draw_trackbars

output_file = 'output.mp4'

fourcc = cv2.VideoWriter_fourcc(*'MP42')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (0, 0))

is_debug = True

# parameters threshold
blur_size = 5
threshold_size = 5
threshold_c = 4
pixel_count = 10


def adjust_blur_size(value):
    global blur_size
    if value % 2 == 1:
        blur_size = value


def adjust_threshold_size(value):
    global threshold_size
    if value % 2 == 1:
        threshold_size = value


def adjust_threshold_c(value):
    global threshold_c
    threshold_c = value


def adjust_pixel_count(value):
    global pixel_count
    pixel_count = value


def set_frame_size(frame_size):
    global out
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (int(frame_size[0]), int(frame_size[1])))


def process_frame(last_frame, current_frame):
    global out
    global pixel_count
    global blur_size

    if last_frame is None:
        return current_frame

    diff = cv2.absdiff(last_frame, current_frame)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)

    threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, threshold_size,
                                      threshold_c)

    non_zero_pixels = cv2.countNonZero(threshold)

    frame = current_frame.copy()

    if non_zero_pixels < pixel_count:
        cv2.line(frame, (0, 0), (current_frame.shape[1], current_frame.shape[0]), (0, 0, 255), 5)
        cv2.line(frame, (0, current_frame.shape[0]), (current_frame.shape[1], 0), (0, 0, 255), 5)
    else:
        out.write(current_frame)

    cv2.imshow('frame', frame)

    if is_debug:
        cv2.imshow('diff', diff)
        cv2.imshow('gray', gray)
        cv2.imshow('blur', blur)
        cv2.imshow('threshold', threshold)


def main():
    if is_debug:
        draw_trackbars(adjust_blur_size, adjust_threshold_size, adjust_threshold_c, adjust_pixel_count)

    noisy_video_path = 'D:/Videos/Music Events Application/metallica-master-of-puppets-live.mp4'
    less_noisy_video_path = 'D:/Videos/Music Events Application/alinacraciunmp4.mp4'

    capture_video(process_frame, set_frame_size)

    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
