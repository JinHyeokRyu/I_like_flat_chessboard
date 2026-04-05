import cv2 as cv
import numpy as np

def select_img_from_video(video_file, wait_msec=10):
    # open video file
    video = cv.VideoCapture(video_file)

    img_select = []
    frame_cnt = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        
        if frame_cnt % wait_msec:
            frame_cnt += 1
            continue
        
        img_select.append(frame.copy())
        frame_cnt += 1

    return img_select


def calib_camera_from_chessboard(images, board_pattern, board_cellsize, K=None, dist_coeff=None, calib_flags=None):
    img_points = []
    for img in images:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        complete, pts = cv.findChessboardCorners(gray, board_pattern)
        if complete:
            img_points.append(pts)
    assert len(img_points) > 0, 'There is no set of complete chessboard points!'

    obj_pts = [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
    obj_points = [np.array(obj_pts, dtype=np.float32) * board_cellsize] * len(img_points)

    return cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], K, dist_coeff, flags=calib_flags)


def save_undistorted(video_file, save_path, K, dist_coeff):
    # open video file
    video = cv.VideoCapture(video_file)

    # 
    fps = video.get(cv.CAP_PROP_FPS)
    w = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    writer = cv.VideoWriter(save_path, fourcc, fps, (w, h))

    ret, frame = video.read()
    h, w = frame.shape[:2]

    map1, map2 = None, None

    while True:
        ret, frame = video.read()
        if not ret:
            break

        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (w, h), cv.CV_16SC2)
        rectified = cv.remap(frame, map1, map2, cv.INTER_LINEAR)

        writer.write(rectified)

    video.release()
    writer.release()
    print("Saved to:", save_path)


if __name__ == "__main__":
    
    video_file = "test.mp4"
    board_pattern = (10, 7)
    board_cellsize = 0.025

    imgs = select_img_from_video(video_file)
    rmse, K, dist_coeff, rvecs, tvecs = calib_camera_from_chessboard(imgs, board_pattern, board_cellsize)

    print('## Camera Calibration Results')
    print(f'* The number of applied images = {len(imgs)}')
    print(f'* RMS error = {rmse}')
    print('* Camera matrix (K) = ')
    print(K)
    print(f'* Distortion coefficient (k1, k2, p1, p2, k3, ...) = {dist_coeff}')

    save_path = "undistorted.mp4"
    save_undistorted(video_file, save_path, K, dist_coeff)