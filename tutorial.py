# import math
# print(math.pi)

# 라이브러리 중 일부만 사용시 import하는 방법
from math import pi

# pi (원주율) 값이 출력된다
print(pi)

# 1. 변수, 배열, 딕셔너리

v1 = 1
print(v1)
v2 = 2
print(v2)

v3 = v1 + v2
print(v3)

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)

d1 = 3.14
d2 = 1.59
d3 = d1 + d2
print(d3)

# object

o1 = [1, 2, 3]
o2 = {"name": "Alice", "age": 30}
combine = {
    "numbers": o1,
    "info": o2
}
print(combine)

# ??? type safe 한지 어떻게 암?
# Python은 동적 타이핑 언어이기 때문에 변수의 타입을 명시적으로 선언하지 않아도 됩니다.
# 변수는 할당된 값에 따라 자동으로 타입이 결정됩니다.
# 예를 들어, v1에 정수를 할당하면 v1은 정수 타입이 되고, s1에 문자열을 할당하면 s1은 문자열 타입이 됩니다.
# 그러나, Python은 타입 힌트를 제공하여 변수의 예상 타입을 명시할 수 있습니다.
# 예를 들어, v1: int = 1과 같이 작성하면 v1이 정수 타입임을 명시할 수 있습니다.
# 하지만, 이는 타입 검사를 위한 힌트일 뿐이며, 실제로 변수의 타입을 강제하지는 않습니다.
# 따라서, Python은 엄격한 타입 검사를 수행하지 않으며, 개발자가 변수의 타입을 신경 써야 합니다.

# 재정의 하면 어떻게 될까?
o1 = {"new_key": "new_value"}
print(o1)  # 이제 o1은 리스트가 아닌 딕셔너리가 됩니다

ss1 = "Im a string"
nn1 = 180

o2 = {
    "name"  : ss1,
    "value" : nn1
}
print(o2)

# 오류나는지 확인
# python 에서 try except 문법
try:
    object1 = [1, 2, 3]
    n1 = 1234
    result = object1 + n1  # 리스트와 정수의 덧셈은 불가능
except Exception as e:
    print("오류 발생:", e)

# object array

o1 = [1, 2,3,4]
print(o1)
o2 = ["apple", "banana", "cherry"]
print(o2)
o3 = [o1, o2]
print(o3)

o3.remove(o1)
print(o3)
o3.append({"new": "object"})
print(o3)

o3.append(1)
print(o3)
o3.append("string")
print(o3)

d = {}
d["a"] = "apple"
d["b"] = "banana"

print(d["a"])
print(d.get("b"))

# 2. 함수

def call(name,value):
    print("Function called with", name, "and", value)
    result = {name:value}
    return result
res = call("test", 123)
print("Function returned:", res)

def sum(a,b):
    return a + b

result = sum(10, 20)
print("Sum result:", result)

# 3. 조건문

n1 = 10
n2 = 20

if n1 < n2:
    print(n1, "is less than", n2)
elif n1 == n2:
    print(n1, "is equal to", n2)
else:
    print(n1, "is greater than", n2)

a = None
if a is None:
    print("a is None")
else:
    print("a is not None")

# 4. 반복문
print("===================")

a = None
i = 1
while a is None:
    print("a is not None")
    i = i + 1
    if i > 5:
        a = 123

print("end")

for i in range(5):
    print("Iteration:", i)

aliens = ["alien1", "alien2", "alien3"]
for alien in aliens:
    print("Alien:", alien)

print("==================")
for index, alien in enumerate(aliens):
    print("Alien", index, "is", alien)
    # break
    if index == 1:
        print("Breaking the loop at index 1")
        break

# 5. 클래스
print("==================")

class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"현재 속도: {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"현재 속도: {self.speed} km/h")

# 객체 생성
my_car = Car("red")
my_car.accelerate()
my_car.brake()

your_car = Car("blue", 50)
your_car.accelerate()
your_car.brake()

carList = [my_car, your_car]
for index, car in enumerate(carList):
    print(f"Car {index} is {car.color} with speed {car.speed} km/h")