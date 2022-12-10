import numpy as np

# 0 1 2
# 3 4 5
# 6 7 8 행렬 생성
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# 4 4 4 행렬 생성
b = np.array([[4], [4], [4]])

hap = a+b  # 3x3 행렬
gop = a.dot(b)  # 3x1 행렬

# 합
print(f"--합의 1행 1,2열, 2행 1,2열--\n{hap[0:2, 0:2]}")
print(f"--합의 2행 2,3열, 3행 2,3열--\n{hap[1:3, 1:3]}\n")
# 곱
print(f"--곱의 1행 1,2열, 2행 1,2열--\n{gop[0:2, 0:2]}")
print(f"--곱의 2행 2,3열, 3행 2,3열--\n{gop[1:3, 1:3]}")
