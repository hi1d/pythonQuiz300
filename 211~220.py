# 211
# 함수의 호출 결과를 예측하라.

# def 함수(문자열):
#     print(문자열)


# 함수("안녕")
# 함수("Hi")

# 안녕
# Hi

# 212
# 함수의 호출 결과를 예측하라.

# def 함수(a, b):
#     print(a + b)


# 함수(3, 4)
# 함수(7, 8)

# 7
# 15

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# 함수 호출 시 정의와 다르게 인자가 들어오지 않아 발생하는 오류


# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# TypeError: must be str, not int

# 함수 호출 시 정의와 다르게, 다른 타입의 값을 전달하여 발생하는 오류

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

def print_with_smile(str):
    return print(str+":D")

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.


print_with_smile("안녕하세요")


# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

def print_upper_price(int):
    return print(int*1.3)


print_upper_price(100)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.


def print_sum(x, y):
    return print(x+y)


print_sum(1, 4)

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75


def print_arithmetic_operation(x, y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)


print_arithmetic_operation(3, 4)

# 220

# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.


def print_max(x, y, z):
    if x > y and x > z:
        return print(x)
    elif y > x and y > z:
        return print(y)
    else:
        return print(z)


print_max(5, 4, 3)
