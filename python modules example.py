#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
import datetime
import glob

print(glob.glob("*.py"))


# os : 운영체제에서 제공하는 기본 기능
import os

print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("already exists")
else:
    os.mkdir(folder)


# time : 시간 관련 함수
import time

print(time.localtime())
print(time.strftime("%Y.%m.%d %H:%M:%S"))


# timedelta : 날짜 계산

today = datetime.date.today()

td = datetime.timedelta(days = 100)

print(today + td)

