import datetime

# 현재 시간 출력
now = datetime.datetime.now()

print("현재 시간 출력")
print(f"지금 시간은 {now.strftime('%Y-%m-%d %H:%M:%S')}.")