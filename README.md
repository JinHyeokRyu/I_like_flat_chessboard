# Cartoon generator

Cartoon generator는 이미지를 만화 스타일로 변환하는 프로그램입니다.<br>


## 변환된 이미지

### 좋은 예시

| Before | After |
|--------|-------|
| <img src='img.jpg' width=450> | ![](img_cartoon.png) |

객체의 경계가 뚜렷하고 단조로워 edge detection이 잘 수행되어 만화 같은 분위기가 잘 나타납니다.

### 아쉬운 예시

| Before | After |
|--------|-------|
| <img src='tree.jpg' width=440> | ![](tree_cartoon.png) |

edge가 많고 복잡한 이미지의 경우, edge 표현이 노이즈처럼 표현되어 오히려 사진이 어두워지고 지저분해 보입니다.


## 개선할만한 점

단조로운 이미지와 복잡한 이미지 모두에서 잘 동작할 수 있도록, blur 처리나 border line의 두께를 더 얇게 조정하면 다양한 성격의 이미지도 만화같은 분위기로 변환할 수 있습니다.


## Camera Calibration Results
* The number of applied images = 58
* RMS error = 1.6542274858249981
* Camera matrix (K) =
[[1.99289143e+03 0.00000000e+00 5.22590339e+02]
 [0.00000000e+00 1.96989478e+03 7.16385708e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [[-0.63361241 -0.41990132  0.0048716   0.0057259   0.98918922]]