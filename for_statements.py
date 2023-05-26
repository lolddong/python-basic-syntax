# for문의 기본 구조
#   for 변수 in 반복가능한자료형(iterable): #예) list, cell, etc.
#       실행문
# 예)
    # lista = [10, 20, 30]
    # for 
    #  in lista:
    #     print(변수)
    #     >> 10
    #     >> 20
    #     >> 30
    # for a in [1, 3, 10]:
    #     print (a)

# range 문법: range(x, y) x 이상 y 미만
    # iterable한 객체 -> list로 변환 가능
    # 예)
        # for a in range(1, 5):
        #     print(a)
        # >>  1
        #     2
        #     3
        #     4
v1 = list(range(1, 5))
print(v1)
