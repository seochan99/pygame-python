# 사다리 알고리즘
import time
import random

# 선발대 운영진
# YB : 23명
OBLikelion = ["김용현", "김은식", "노종원", "조지연", "김성준",
              "서정연", "이광빈", "김범기", "김보배", "송수민",
              "장성원", "정신우", "박현준", "이주영", "정미혜",
              "강협", "송요민", "이소정", "윤상우", "이형석",
              "임도연", "주현이", "양지우"]

# 선발대 학생
# OB : 20명
YBLikelion = ["정준홍", "김태연", "강동희", "김수영", "이지영",
              "신예진", "이건회", "안소은", "이여원", "정민주",
              "정재혁", "김윤성", "김재니", "박영신", "안유성",
              "오민영", "오준서", "윤영서", "이영서", "이예나",
              "", ""]


random.shuffle(OBLikelion)
random.shuffle(YBLikelion)

print("💡 짝 궁 💡")

for i in range(1, 23):
    print(f"{i}팀 : [OB]{OBLikelion[i]}, [YB]{YBLikelion[i]}")
    # time.sleep(1)
