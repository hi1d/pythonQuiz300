# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
# Account 클래스를 생성한 후 생성자를 구현해보세요.
# 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

from abc import get_cache_token
import random


class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
# 은행이름: SC은행
# 계좌번호: 111-11-111111


kim = Account('gunwoo', '10000')
print(kim.name)
print(kim.money)
print(kim.bank)
print(kim.account_number)


# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1


kim = Account('gunwoo', '10000')
kim = Account('minwoo', '100000')
print(Account.account_total_count)


# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)


kim = Account('gunwoo', '10000')
Account.get_account_num()


# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)

    def deposit(self, money):
        if money >= 1:
            self.money += int(money)
        else:
            print("1원 이상만 입금이 가능합니다.")


kim = Account('gunwoo', 10000)
print(kim.money)
kim.deposit(10)
print(kim.money)

# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.


class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)

    def deposit(self, money):
        if money >= 1:
            self.money += int(money)
        else:
            print("1원 이상만 입금이 가능합니다.")

    def withdraw(self, money):
        if money > self.money:
            print("잔고 이상은 출금할 수 없습니다.")
        else:
            self.money -= money


kim = Account('gunwoo', 10000)
print(kim.money)
kim.withdraw(100000)
kim.withdraw(900)
print(kim.money)

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요.


class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)

    def deposit(self, money):
        if money >= 1:
            self.money += int(money)
        else:
            print("1원 이상만 입금이 가능합니다.")

    def withdraw(self, money):
        if money > self.money:
            print("잔고 이상은 출금할 수 없습니다.")
        else:
            self.money -= money

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.money}")

        # print(f"잔고: {self.money}")

# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10000원


kim = Account('gunwoo', 10000)
kim.display_info()


# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.deposit_count = 0
        self.name = name
        self.money = int(money)
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)

    def deposit(self, money):
        if money >= 1:
            self.money += int(money)

            self.deposit_count += 1
            if self.deposit_count == 5:
                self.money += self.money*0.01
                self.deposit_count = 0
        else:
            print("1원 이상만 입금이 가능합니다.")

    def withdraw(self, money):
        if money > self.money:
            print("잔고 이상은 출금할 수 없습니다.")
        else:
            self.money -= money

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.money}")


kim = Account('gunwoo', 10000)
print(kim.money)
kim.deposit(10)
kim.deposit(10)
kim.deposit(10)
kim.deposit(10)
kim.deposit(10)
print(kim.money)

# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

kim = Account('gunwoo', 10000)
lee = Account('gunwoo', 1000000)
park = Account('gunwoo', 10000000)

account_list = [kim, lee, park]


# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

for i in account_list:
    if i.money >= 1000000:
        i.display_info()
    else:
        continue


# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요.
# 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

class Account:
    account_total_count = 0

    def __init__(self, name, money):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.money = int(money)
        self.bank = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3
        Account.account_total_count += 1

    def get_account_num():
        return print(Account.account_total_count)

    def deposit(self, money):
        if money >= 1:
            self.money += int(money)

            self.deposit_count += 1
            if self.deposit_count == 5:
                self.money += self.money*0.01
                self.deposit_count = 0
            self.deposit_log.append(money)
        else:
            print("1원 이상만 입금이 가능합니다.")

    def withdraw(self, money):
        if money > self.money:
            print("잔고 이상은 출금할 수 없습니다.")
        else:
            self.money -= money
            self.withdraw_log.append(money)

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.money}")

    def deposit_history(self):
        for i in self.deposit_log:
            print(i)

    def withdraw_history(self):
        for i in self.withdraw_log:
            print(i)


kim = Account('gunwoo', 10000)
kim.deposit(100)
kim.deposit(200)
kim.deposit(300)
kim.deposit(400)
kim.deposit(500)
kim.deposit_history()

kim.withdraw(10)
kim.withdraw(20)
kim.withdraw(30)
kim.withdraw(40)
kim.withdraw(50)
kim.withdraw(60)
kim.withdraw_history()
