# 사다리 알고리즘
import time
import random

# 선발대 운영진
# YB : 23명
OBLikelion = ["1팀","2팀"]

# 선발대 학생
# OB : 20명
babyLion = ["김윤서(3)","곽호은(3)","이창준(4)","박지호(4)","심서현(3)","김동환(2)","오찬주(2)",
            "김혜수(3)","차승민(2)","설현아(2)","이유진(3)","김민성(3)","김강민(2)","양지원(3)",
            "박서희(4)","최준형(3)","윤혜정(3휴)","이주원(3)","박호연","배지현","정세윤","김민준",
            "조민우","서지은","차은호","이상준","유수민","최나래","이종범","전병현"]

# 7팀 : 4,4,4,4,5,5,4


random.shuffle(babyLion)

print("💡 짝 궁 💡\n")
time.sleep(2)
print(f"1팀 : {babyLion[0:4]}\n")
time.sleep(2)
print(f"2팀 : {babyLion[4:9]}\n")
time.sleep(2)
print(f"3팀 : {babyLion[9:13]}\n")
time.sleep(2)
print(f"4팀 : {babyLion[13:17]}\n")
time.sleep(2)
print(f"5팀 : {babyLion[17:22]}\n")
time.sleep(2)
print(f"6팀 : {babyLion[22:26]}\n")
time.sleep(2)
print(f"7팀 : {babyLion[26:30]}\n")
time.sleep(2)
