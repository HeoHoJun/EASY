# |이 코드는 상속을 이용하여 부모 클래스인 Person 클래스를 상속받아 자식 클래스인 Ai_Students 클래스를 정의하고 있습니다.
# |
# |좋은 점:
# |- 코드의 재사용성이 높아졌습니다. 부모 클래스에서 정의한 속성과 메서드를 자식 클래스에서 그대로 사용할 수 있습니다.
# |- 코드의 가독성이 높아졌습니다. 부모 클래스에서 정의한 속성과 메서드를 자식 클래스에서 그대로 사용할 수 있으므로 코드의 중복을 줄일 수 있습니다.
# |
# |나쁜 점:
# |- 자식 클래스에서 부모 클래스의 __init__ 메서드를 오버라이딩하고 있습니다. 이 경우, 부모 클래스에서 정의한 속성을 초기화하지 않고 자식 클래스에서 새로운 속성을 추가하면 부모 클래스에서 정의한 속성이 초기화되지 않아 오류가 발생할 수 있습니다. 이를 방지하기 위해서는 super() 함수를 이용하여 부모 클래스의 __init__ 메서드를 호출해야 합니다.
class Person:
    def __init__(self, name, age): # Person 클래스 생성자
        self.name = name # 이름 속성
        self.age = age # 나이 속성
        
class Ai_Students(Person):
    def __init__(self, name, age, sex): # Ai_Students 클래스 생성자
        super().__init__(name, age) # 부모 클래스(Person)의 생성자 호출
        self.sex = sex # 성별 속성

p1 = Person("yo", 29) # Person 클래스의 인스턴스 생성
p2 = Ai_Students("HeoHoJun", 34, "man") # Ai_Students 클래스의 인스턴스 생성

print(p1.name, p1.age) # yo 29 출력
print(p2.name, p2.age, p2.sex) # HeoHoJun 34 man 출력