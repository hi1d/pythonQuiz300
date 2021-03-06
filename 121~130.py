# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.

# >> a
# A
# 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다.
# 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다.
# 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.

import requests
# str_one = input()
# if str_one.islower() is True:
#     str_one = str_one.upper()
#     print(str_one)
# else:
#     str_one = str_one.lower()
#     print(str_one)


# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.

# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A

# score = input()
# score = int(score)
# if 81 <= score <= 100:
#     print("grade is A")
# elif 61 <= score <= 80:
#     print("grade is B")
# elif 41 <= score <= 60:
#     print("grade is C")
# elif 21 <= score <= 40:
#     print("grade is D")
# elif 0 <= score <= 20:
#     print("grade is E")


# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
# 각 통화별 환율은 다음과 같다.
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	    환율
# 달러	        1167
# 엔	        1.096
# 유로	        1268
# 위안	        171
# >> 입력: 100 달러
# 116700.00 원

# user = input()
# rate = [1167, 1.096, 1268, 171]
# user_split = user.split(' ')
# result = 0
# for i in range(len(user_split)):
#     result += float(rate[i] * int(user_split[i]))

# print(result)

# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
# num_list = []
# for i in range(3):
#     num = input()
#     num_list.append(num)
# print(max(num_list))


# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고,
# 통신사를 출력하는 프로그램을 작성하라.

# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.

# phone = input("휴대전화 번호 입력:")
# 통신사 = phone.split('-')[0]
# result = ''
# if 통신사 == '011':
#     result = 'SKT'
# elif 통신사 == '016':
#     result = 'KT'
# elif 통신사 == '019':
#     result = 'LGU'
# elif 통신사 == '010':
#     result = '알수없음'

# print(f"당신은 {result} 사용자입니다.")

# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

# -	    0	    1	  2 	 3	    4	  5 	6  	  7 	8      9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
# >> 우편번호: 01400
# 도봉구
# gu = {
#     0: '강북구',
#     1: '강북구',
#     2: '강북구',
#     3: '도봉구',
#     4: '도봉구',
#     5: '도봉구',
#     6: '노원구',
#     7: '노원구',
#     8: '노원구',
#     9: '노원구',
# }

# address_num = input("우편번호: ")
# address_num = int(address_num[2:3])
# print(gu[address_num])

# 127
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 남자
# num = input("주민등록번호: ")
# num = int(num.split('-')[1][:1])
# print(num)
# if num == 1 or num == 3:
#     print("남자")
# elif num == 2 or num == 4:
#     print("여자")

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.
# num = input("주민등록번호: ")
# num = int(num.split('-')[1][1:3])
# if 0 <= num <= 8:
#     print("서울 입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5)
# = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.
# 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다.

# check = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# num = input("주민등록번호: ")
# num = (num.split('-'))
# num = ''.join(num)
# num_sum = 0
# for i in range(len(num)-1):
#     num_sum += int(num[i])*check[i]

# if str(11-(num_sum % 11)) == num[-1]:
#     print("유효한 주민등록번호 입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# 130
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우
# "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# Key Name	    Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	    최근 24시간 내 최저 거래금액
# max_price	    최근 24시간 내 최고 거래금액

max_price = int(btc['max_price'])
price_range = int(btc['max_price']) - int(btc['min_price'])
open_price = int(btc['opening_price'])

if max_price < open_price+price_range:
    print("상승장")
else:
    print("하락장")
