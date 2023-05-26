# if문의 기본 구조
# (else는 optional 요소)
#   if 참 조건:
#       실행문
#   else:
#       실행문
# 예)
    # a = int(input("a는 무슨 숫자입니까?"))
    # if a>10:
    #     print("a는 10보다 큽니다.")
    # else: 
    #     print("a는 10보다 작습니다.")

    # trueOrFalse = True
    # if trueOrFalse:
    #     print("참입니다.")
    # else:
    #     print("거짓입니다.")

    # money = int(input("얼마를 가지고 있습니까?"))
    # if money > 30000:
    #     print("택시를 타고 가시오.")
    # else:
    #     print("걸어가시오.")

# 비트연산이란 2진법의 숫자를 |(or), &(and), ^(xor) 등으로 CPU 내부적으로 계산하는 방식
    # a = 10
    # if (a > 5) | (a > 100):       # 반드시 () 해줘야 됨
    #     print("참입니다.")
    # >> 참입니다.
    # if a > 5 or a > 100:
    #     print("참입니다.")
    # >> 참입니다.

    # and는 &, or는 |, not은 부정의 의미
    # 비트연산을 할 때에는 기호를 써야 된다 (and, or, not이 아니라 - 조금 다른 방식/의미로 쓰임)
    # not True는 False, not False는 True

    # 1111 & 1000 => 1000
    # 1111 | 1000 => 1111

# 대입 연산자
    # a = 10
    # a += 1        # a = a + 1 과 동일
    # print(a)
    # >> 11
    # print(a += 1)
    # >> SyntaxError: invalid syntax
    # -= /= *= 도 동일

# 비교 연산자
    # chaining (범위 표현 가능, 몇 다른 언어에서는 표현 불가능)
        # 5 < a < 100       # a > 5 and 100 < a 와 동일
a = 10
if 5 < a < 100:
    print("참입니다.")

# for문의 기본 구조
#   for 변수 in 반복가능한자료형(iterable): #예) list, cell, etc.
#       실행문
# 예)
    # lista = [10, 20, 30]
    # for 변수 in lista:
    #     print(변수)
    #     >> 10
    #     >> 20
    #     >> 30
    # for a in [1, 3, 10]:
    #     print (a)

    # range 문법: range(x, y) x 이상 y 미만
    # for a in range(1, 101):
        # print(a)

