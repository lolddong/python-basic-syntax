# # 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
# # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# # 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# # 제한사항
# # sides의 원소는 자연수입니다.
# # sides의 길이는 2입니다.
# # 1 ≤ sides의 원소 ≤ 1,000

# # sides=[1, 2]
# # # result =1
# # sides = [3, 6]	
# # # result = 5
# sides = [11, 7]	
# # result = 13

# # 입출력 예 #1

# # 두 변이 1, 2 인 경우 삼각형을 완성시키려면 나머지 한 변이 2여야 합니다. 따라서 1을 return합니다.
# # 입출력 예 #2

# # 가장 긴 변이 6인 경우
# # 될 수 있는 나머지 한 변은 4, 5, 6 로 3개입니다.
# # 나머지 한 변이 가장 긴 변인 경우
# # 될 수 있는 한 변은 7, 8 로 2개입니다.
# # 따라서 3 + 2 = 5를 return합니다.
# # 입출력 예 #3

# # 가장 긴 변이 11인 경우
# # 될 수 있는 나머지 한 변은 5, 6, 7, 8, 9, 10, 11 로 7개입니다.
# # 나머지 한 변이 가장 긴 변인 경우
# # 될 수 있는 한 변은 12, 13, 14, 15, 16, 17 로 6개입니다.
# # 따라서 7 + 6 = 13을 return합니다.



# count = 0
# sides.sort()
# for a in range(1, 1001):
#     if (a < (sides[0] + sides[1])) and (a > sides[1]):
#         count += 1
# for b in range(1, 1001):
#     if (sides[1] < (sides[0] + b)) and (sides[1] >= b) and (sides[1] >= sides[0]):
#         count += 1
# print(count)




spell = ["p", "o", "s"]	
dic = ["sod", "eocd", "qixm", "adio", "soo"]
# result = 2
# spell = ["z", "d", "x"]	
# dic = ["def", "dww", "dzx", "loveaw"]
# #result = 1
# spell = ["s", "o", "m", "d"]
# dic = ["moos", "dzx", "smm", "sunmmo", "som"]	
# # result = 2

lista = []
listb = []
listc = []
listd = []
for a in range(len(spell)):
    for b in range(len(dic)):
        if (spell[a] in dic[b]):
            lista.append(dic[b].replace(spell[a], '1'))
            dic[b] = dic[b].replace(dic[b], "")
print(lista)
for a in range(len(spell)):
    for b in range(len(lista)):
        if (spell[a] in lista[b]):
            listb.append(lista[b].replace(spell[a], '1'))
for a in range(len(spell)):
    for b in range(len(listb)):
        if (spell[a] in listb[b]):
            listc.append(listb[b].replace(spell[a], '1'))
for a in range(len(spell)):
    for b in range(len(listc)):
        if (spell[a] in listc[b]):
            listd.append(listc[b].replace(spell[a], '1'))
print(listd)