
f = open("tips.csv", "r", encoding="UTF-8")
lines = f.readlines()                                 # f.readlines() - 데이터를 리스트형태로 라인별로 담아준다
# lista = []
# listb = []
print(f.readlines())
# for a in range(1, 246):
#     lista.append(lines[a])
# for b in lista:
#     listb.append(b.split(','))
# print(listb)
# for a in listb:
#     a[-1] = a[-1].replace('\n', '')
#     listb[a].append(a[-1])
#     del listb[a][-2]
#     print(listb[a])

    # a.append(str(float(a[1])/float(a[0])))
    # print(",".join(a))
            # st2 = st1.join(lista)


# f = open("tips.csv", "a", encoding="UTF-8")
# for i in range(2, 245):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()