# for문의 기본 구조
    # 예)
        # for 변수 in 반복가능한자료형(iterable): #예) list, cell, tuple, string
        #   실행문
    # 예)
        # lista = [10, 20, 30]
        # for a in lista:
        #     print(a)
        #     >> 10
        #     >> 20
        #     >> 30
    # for a in list 구문으로는 원본리스트 데이터 변경 불가
        # 예) 아래와 같은 방식으로는 원본 lista의 값 변경 불가
            # lista = [10, 20, 30, 40]
            # for a in lista:
            #     a = 100 
        # 아래와 같은 방식으로 해야 원본리스트 데이터 변경
            # lista = [10, 20, 30, 40]
            # for a in range(len(lista)):
            #     lista[a] = 100
            # print(lista)
            # >> [100, 100, 100, 100]
        # 또는 while문 사용
            # lista = [10, 20, 30, 40]
            # indexTemp = 0
            # while indexTemp < len(lista):
            #     lista[indexTemp] = 100
            #     indexTemp += 1
            # print(lista)

lista = [10, 20, 30, 40]
for a in lista:
    a = 100 
print(lista)
# range 문법
    # range(x, y) - x 이상 y 미만의 숫자를 담은 객체
    # range(y) - 0 이상 y 미만의 숫자를 담은 객체
    # iterable한 객체 -> list로 변환 가능
    # range를 list로 바꾸기 - list()
        # v1 = list(range(1, 5))
        # print(v1)
        # >> [1, 2, 3, 4]

# 연습 문제
# for a in list를 써서 v1의 값 모두 출력
    # v1 = list(range(10, 20))
    # for a in v1:
    #     print(a)
    # for a in range(0, len(v1)):
    #     print(v1[a])
    



