users = [
    {"name": "철수", "age": 25, "height": 172.2},
    {"name": "영희", "age": 18, "height": 152.4},
    {"name": "민수", "age": 30, "height": 168.3},
    {"name": "지수", "age": 15, "height": 163.7}
]

def check_adult(name, age):  #def로 함수 지정하기 (check_adult 실행 시 아래 내용 실행)
    if age >= 20:
        return f"{name}님은 성인입니다."
    else:
        return f"{name}님은 미성년자입니다."
    
result1 = check_adult("지수", 15) #name에 지수 age에 15가 들어간 check_adult 실행
result2 = check_adult("민수", 30)

def list_check():
    for i in users: #users 리스트 모두 검사
        print(check_adult(i["name"], i["age"])) #name과 age만 check_adult에 입력

print(result1)
print(result2)
list_check()