name = str(input("이름을 입력하세요: "))  # 문자열 (String)
age = int(input("나이를 입력하세요: "))         # 정수 (Integer)
height = float(input("키를 입력하세요: "))   # 실수 (Float)
man = True # 불리언 (Boolean - 참/거짓)
adult = True
sex = str(input("성별을 입력하세요: "))
if sex == "여자": #~라면 실행 (if)
    man = False

if age < 20:
    adult = False

print(f"{name}의 나이는 {age}살이고, 키는 {height}cm야.")
print(f"남자인가요? {man}")
print(f"성인인가요? {adult}")