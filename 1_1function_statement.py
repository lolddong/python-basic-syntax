
# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자
# 그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자
# 복잡한 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자
# 옵션: input 과 return 값이 있거나 없어도 됨
    # input과 return 있는 경우
        # def myFunc(myInput):                                    # def 함수명(입력값):            # 예)
        #     calc = (((myInput + 10) * 20) / 10) ** 2            #   answer = 복잡한 로직         #     max()
        #     return calc                                         #   return answer             #     min() 
    # input과 return 없는 경우                                       # def 함수명():                # 예)
        # def hello():                                            #    복잡한 로직                 #    .sort()  
        #     print("hello")
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출
# 연습
    # 함수명: myPlusFunc; 함수의 로직: 사용자의 input을 받아 input값의 누적합을 더하는 함수
    # 예) 100을 입력하면 1+2+3+...+100 의 값을 구하는 함수
        # def myPlusFunc(num):
        #     return sum(list(range(1, num+1)))
    # input값 2개를 받아 2값을 더한 뒤, *2만큼 하여 return하는 함수
    # 그리고, 해당 함수를 호출하여 호출된 결과값은 result에 담아 출력
        # def sumTimesTwo(num1, num2):
        #     return (num1 + num2)*2

# list의 index함수를 쓰지 않고 for문 또는 while문을 통해 숫자 9가 몇번째 index에 있는 값인지 print보자 
    # .index() 쓰기
        # lista = [1, 4, 6, 9]
        # print(lista.index(9))
    # while 쓰기
        # lista = [1, 4, 6, 9]
        # a = 0
        # while a < len(lista):
        #     if lista[a] == 9:
        #         print(a)
        #         break
        #     else:
        #         a += 1
    # for 쓰기
        # lista = [1, 4, 6, 9]
        # for a in range(len(lista)):
        #     if lista[a] == 9:
        #         print(a)
        #         break                 # break를 넣어줘야 가장 첫 9의 인덱스만 출력: break 안 걸 시 뒤에 있는 9의 인덱스도 출력
    # 위의 for/while문을 활용하여 myIndex라는 이름의 함수 만들기, input 값 2개(list, 변수); print는 함수 내에서 하지 않고 return에 값을 담는다
def myIndex(lista, num):
    result = -1
    for a in range(len(lista)):
        if lista[a] == num:
            result = a
            break 
    return result
print(myIndex([1, 2, 9, 4], 9))