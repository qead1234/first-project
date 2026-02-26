users = [
    {"name": "철수", "age": 25, "height": 172.2},
    {"name": "영희", "age": 18, "height": 152.4},
    {"name": "민수", "age": 30, "height": 168.3},
    {"name": "지수", "age": 15, "height": 163.7}
]
#list 생성 (변수 = [])

for user in users:
    name = user["name"]
    age = user["age"]  #변수에 리스트의 name, age에 대응하는 값 지정
    height = user["height"]
    
    if age >= 20:
        print(f"{name}님은 성인입니다.")
    else:
        print(f"{name}님은 미성년자입니다.")

    if height >= 160:
        print(f"{name}님의 키는 160 이상입니다.")
    else:
        print(f"{name}님의 키는 160 미만입니다.")