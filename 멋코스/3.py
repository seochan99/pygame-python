# #선택 정렬 
# from cmath import pi
# import imp
# from re import L
# import re
# import sys


# arr = [7,5,9,0,3,1,6,2,4,8]

# for i in range(len(arr)):
#     min_index = i 
#     for j in range(i +1,len(arr)):
#         if arr[min_index]>arr[j]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index],arr[i] #swap
# print(arr)

# 삽입 정렬 
# for i in range(1,len(arr)):
#     for j in range(i,0,-1): 
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#         else :
#             break 
# print(arr)

#퀵 정렬 
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr 
#     pivot = arr[0]
#     tail = arr[1:] 

#     left_side = [x for x in tail if x<= pivot]
#     right_side = [x for x in tail if x>pivot]

#     return quick_sort(left_side)+[pivot]+quick_sort(right_side)
# print(quick_sort(arr))


# 계수 정렬 
# count = [0] * (max(arr)+1)
# for i in range(len(arr)):
#     count[arr[i]]+=1 

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i,end=" ")

# 두 배열의 원소 교체 
# n,k = map(int,input().split())
# a= list(map(int,input().split()))
# b= list(map(int,input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i]<b[i]:
#         a[i],b[i] = b[i],a[i] #두 변수 스왑스킬 
#     else :
#         break 
# print(sum(a))


# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n,m = map(int,input().split()) ; cnt=0 

#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     a.sort(reverse=True)
#     b.sort()
#     for i in a:
#         for j in b:
#             if i>j:
#                 cnt+=1 
#             else :
#                 break 

#     print(cnt)

# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**4) 

# #이분탐색 
# def bsr(target,start,end,data): #
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if data[mid]==target:
#         del data[mid]
#         return 1
#     elif data[mid]>target:
#         end = mid - 1
#     else : #data[mid]<target
#         start = mid + 1 
#     return bsr(target,start,end,data)

n = int(input()) #상근 카드 갯수 
arr1 = list(map(int,input().split()))

m = int(input()) #엠
arr2 = list(map(int,input().split()))

#상근이가 가지고 있으면 1 아니면 0 출력 
arr1.sort()
for i in range(m):
    if bsr(arr2[i],0,n-1,arr1):
        print(1,end=" ")
    else :
        print(0,end=" ")
