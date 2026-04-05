# I like flat Chessboard!

카메라로 인해 왜곡되어 버린 여러분의 Chessboard를 평평하게 만들어드립니다.<br>
본 프로그램은 OpenCV를 기반으로 작성되었습니다.

## Camera Calibration

왜곡된 Chessboard를 평평하게 만들기 위해서는 다양한 각도의 동영상이 필요합니다.<br>
동영상에서 10프레임 단위로 이미지를 추출하여 camera calibration을 수행합니다.

### Camera Calibration Results

camera calibration이 완료되면, 여러분의 camera 정보와 distortion 정보가 출력됩니다.

(예시)
* The number of applied images = 58
* RMS error = 1.6542274858249981
* Camera matrix (K) = <br>
[[1.99289143e+03 0.00000000e+00 5.22590339e+02]<br>
 [0.00000000e+00 1.96989478e+03 7.16385708e+02]<br>
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = <br>[-0.63361241 -0.41990132  0.0048716   0.0057259   0.98918922]

## Distortion Correction

calibration으로 얻은 정보를 이용하여, 우리의 Chessboard를 평평하게 만들어 저장합니다.

## 변환된 동영상

| Before | After |
|--------|-------|
| ![](./test.gif) | ![](undistorted.gif) |

객체의 경계가 뚜렷하고 단조로워 edge detection이 잘 수행되어 만화 같은 분위기가 잘 나타납니다.
