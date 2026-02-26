# 1. 변수: 데이터를 담는 바구니야
name = str(input("이름을 입력하세요: "))  # 문자열 (String)
age = int(input("나이를 입력하세요: "))         # 정수 (Integer)
height = float(input("키를 입력하세요: "))   # 실수 (Float)
man = True # 불리언 (Boolean - 참/거짓)
sex = str(input("성별을 입력하세요: "))
if sex == "여자":
    man = False
# 2. 출력하면서 확인하기
print(f"{name}의 나이는 {age}살이고, 키는 {height}cm야.")
print(f"남자인가요? {man}")