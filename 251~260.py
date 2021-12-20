# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

# 클래스 : 동일한 무엇을 계속 만들어내는 틀과 같은것.(설계도, 도면과 같은것)
# 객체 : 클래스에 의해서 만들어진 실체(실제로 만들어진 제품)
# 인스턴스 : 클래스에 의해서 만들어진 객체(특정 객체가 어떤 클래스의 객체인지 관계위주로 설명 할 때)

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

class Human:
    pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.


areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# >>> areum = Human()
# 응애응애


class Human:
    def __init__(self):
        print("응애응애")


areum = Human()

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("아름", 25, "여자")


# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예

# >>> areum.age
# 25

print(areum.name, areum.age, areum.sex)


# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")


areum = Human("아름", 25, "여자")
areum.who()

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("모름", 0, "모름")
areum.who()

areum.setInfo("아름", 25, "여자")
areum.who()

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")


areum = Human("아름", 25, "여자")
del(areum)

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.


class OMG:
    def print():
        print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given

# 파이썬 인터프리터가 자동으로 메소드를 호출할 때 인자를 넣어버리기에 생기는 오류


myStock = OMG()
OMG.print()

# 또는


class OMG:
    def print(self):
        print("Oh my god")


myStock = OMG()
myStock.print()
