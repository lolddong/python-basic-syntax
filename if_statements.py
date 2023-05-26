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

    # a = 10
    # if (a > 5) | (a > 100):       # 반드시 () 해줘야 됨
    #     print("참입니다.")
    # >> 참입니다.
a = 10
if a > 5 or a > 100:
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

