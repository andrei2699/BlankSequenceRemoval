import cv2


def draw_trackbars(pixel_count, frame_skip):
    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 240)
    cv2.createTrackbar('Pixel count', 'Trackbars', 0, 100000, pixel_count)
    cv2.createTrackbar('Frame skip', 'Trackbars', 0, 10, frame_skip)
