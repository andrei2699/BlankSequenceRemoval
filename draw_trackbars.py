import cv2


def draw_trackbars(blur_size, threshold_size, threshold_c, pixel_count):
    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 240)
    cv2.createTrackbar('Blur size', 'Trackbars', 5, 10, blur_size)
    cv2.createTrackbar('Threshold Size', 'Trackbars', 5, 11, threshold_size)
    cv2.createTrackbar('Threshold C', 'Trackbars', 4, 10, threshold_c)
    cv2.createTrackbar('Pixel Count', 'Trackbars', 1, 100, pixel_count)
