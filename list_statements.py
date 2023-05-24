# list는 변수마다 값을 할당해서 사용하기에 관리의 어려움이 있으므로 한 변수에 값을 집합시켜 놓은 것
# list는 순서가 있고 값의 추가, 삭제, 수정이 가능한 구조를 가지고 있다
# 반면 문자열(예) "hello")은 메모리 내부적으로 list와 유사한 자료구조이나 문자열은 값을 추가하거나 수정할 수가 없다
# list의 경우에 [](대괄호)를 사용하여 데이터를 집합, 내부적으로는 ,(반점)로 구분
# 예)
    # a = "김돌쇠"
    # b = "김갑돌"
    # c = "김갑순"
    # 위 원소들을 한 list에 담아 놓은 것: 하나의 변수로 여러개의 데이터를 관리/집합
    # list = ["김돌쇠", "김갑돌", "김갑순"]
# list 안에는 빈값, 숫자, 문자, 다른 list등이 공존할 수 있다
    # 예) lista = []
    # 예) listb = ['a', 'b', 1, 2, ['hello', 'nice', 'bye']]

# list 안의 각각 값에 접근할 때 index 사용
# lista = ["a", "b", "c", "d", "e", "f"]
#   print(lista[0])
#   print(lista[1])
#   print(lista[2])
#   print(lista[3])
#   print(lista[4])
#   print(lista[5])

# list안에 list의 값을 조회하는 방법
    # list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
    # 1) 변수 number에 [1,2,3]을 담아 출력
        # list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
        # number = list_ex1[-1]
        # print(number)
    # 2) number에 담은 값중 1과 3을 더해 4를 출력
        # print(number[0]+number[2])

# slicing
    # 여러개의 데이터를 범위를 지정해서 가져오고 싶을 때 사용
    # slicing의 결과값은 같은 list로 출력

# 연습
    # 5번째까지 출력
    #   print(lista[:5])
    #   >> ['a', 'b', 'c', 'd', 'e']
    # 5번째까지 출력한 결과물의 type 출력
    #   print(type(lista[:5]))
    #   >> <class 'list'>

