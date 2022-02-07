## 프로그래머스 level 1 : x만큼 간격 

# #내풀이 
# def solution(x,n):
#     answer = []
#     for i in range(n):
#         answer.append(x*(i+1))
#     return answer

# #다른사람풀이 
# def solution(x,n):
#     return [i*x+x for i in range(n)]

# 핸드폰 번호 가리기

# def solution(phone_number):
#     return "*"*(len(phone_number)-4) + phone_number[-4:]

# print(solution("01023624076"))

#행렬의 덧셈 
# def solution(arr1, arr2):
#     answer = [[]]
#     answer.append(arr1[0]+arr2[0])
#     return answer

# num1,num2 = map(int,input().split())
# print("덧셈 :",num1+num2)
# print("뺄셈 :",num1-num2,"이것은 뺄셈입니다.")
# print(f"뺄셈 : {num1-num2} 이것은 뺄셈입니다. ")
# print("곱셈 :",num1*num2)
# print("나눗셈 :",num1//num2)
# print("나머지 :",num1%num2)


#문자열 압축 

# def solution(arr):
#     ans = len(arr)  # 처음 길이 
#     for step in range(1,len(arr)//2+1): #문자열 길이의 절반만큼만 잘라서 확인 ! 그 이후부터는 잘라도 다음 조각이 없음 
#         com = "" #빈문자열 
#         comArr = arr[0:step] 
#         cnt = 1
#         for j in range(step,len(arr),step):
#             if comArr == arr[j:j+step]: #문자열이 동일하다면 
#                 cnt+=1 
#             else: #다른 문자열 나오면 com완성하고 상태초기화 
#                 com += str(cnt) + comArr if cnt>=2 else comArr #2이상일때마다, 1은 생략하니깐 ! 
#                 comArr = arr[j:j+step]
#                 cnt = 1  # 
#         #남아 있는 문자열 붙이기 
#         com += str(cnt)+ comArr if cnt>=2 else comArr 
#         ans = min(ans,len(com))
#     return ans 
# arr = input()

# print(solution(arr))

#자물쇠..
#완전 탐색 

#matrix 90도 회전 함수 
# def rotate_90(a): 
#     n = len(a)
#     m = len(a[0])
#     result = [[0]*n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = a[i][j] 
#     return result 
# #모두 1인지 확인 함수 
# def check(new_lock): 
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length,lock_length * 2):
#         for j in range(lock_length,lock_length*2):
#             if new_lock[i][j] != 1:
#                 return False 
#     return True 
# def solution(key,lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0]*(n*3) for _ in range(n*3)] #새로운 매트릭스 생성 
#     #새 매트릭스 가운데 넣기 
#     for i in range(n):
#         for j in range(m):
#             new_lock[i+n][j+n] = lock[i][j] 
    
#     for rotation in range(4): 
#         key = rotate_90(key) 
#         for x in range(n*2):
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         #열쇠 넣기 
#                         new_lock[x+i][y+j]+=key[i][j]
#                 #확인하기 
#                 if check(new_lock) == True :
#                     return True 
#                 # False 이면 열쇠다시빼기 
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False 

#3190 : 뱀 
# from collections import deque

# #상 우 하 좌
# dy = [-1,0,1,0]
# dx = [0,1,0,-1]
# def change(direct,c):
#     # 상 0 
#     # 우 1
#     # 하 2
#     # 좌 3 
#     # 시계방향 회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향 
#     # 반시꼐 방향 회전 : 상(0) -> 좌(3) ... 
#     if c == "L":
#         direct = (direct - 1) % 4 
#     else :
#         direct = (direct + 1) % 4 
#     return direct

# def start():
#     direct = 1 #초기 방향 
#     time = 1 #게임시간 
#     y,x = 0,0 #초기 뱀 위치 
#     visted = deque([[y,x]])
#     matrix[y][x] = 2
#     while True :
#         y,x = y+dy[direct], x+dx[direct]
#         if 0<=y<n and 0<=x<n and matrix[y][x] != 2:
#             if not matrix[y][x] == 1: #apple X 
#                 temp_y,temp_x = visted.popleft()
#                 matrix[temp_y][temp_x] = 0 # del tail 
#             matrix[y][x] = 2
#             visted.append([y,x])
#             if time in times.keys(): #시간초에 도달하면 
#                 direct = change(direct,times[time]) #방향과 바꿔야하는 방향 전달 
#             time += 1
#         else : #벽에 부딪힘 ㅜㅜ 
#             return time



# n = int(input()) #보드크기 
# k = int(input()) #사과 개수 

# matrix = [[0]*n for _ in range(n)]
# kXY =[]
# for _ in range(k):
#     x,y = map(int,input().split())
#     matrix[x-1][y-1] = 1 #save apple 

# l = int(input()) #방향전환 

# times = {}

# for _ in range(l):
#     x,c = input().split()
#     times[int(x)] = c 

# print(start())