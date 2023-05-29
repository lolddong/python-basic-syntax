a = 3
b = 4
# '3'와 '4'는 정수, '0.75'는 실수
# 파이썬은 정수를 가지고 계산해서 실수 값이 나와도 자동적으로 실수 값을 나타내줌 (다른 언어들은 오류나는 경우 있음)
# 몫: //, 나머지: %
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 자료의 형변환
a = 10
b = 20
# 결과값이 1020이 나오도록 덧셈을 하여라
print(str(a) + str(b))
c = 2.333333
d = 5/4
# c와 d의 소수부분을 잘라서 출력하라
print(int(c))
print(int(d))

# 제곱, 제곱근
# 2의 10 제곱을 출력하라
print(2**10)
print(pow(2,10))
# 제곱근은 math라는 라이브러리를 import해줘야 한다.
import math
# 위는 math라는 라이브러리를 선언하는 것
# pow(a,b) 또한 math 라이브러리에도 있다
print(math.pow(2,10))
# 1024의 제곱근을 구하라
print(math.sqrt(1024))