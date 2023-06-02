
fr= open("tips.csv", "r", encoding="UTF-8")
lines = fr.readlines()                                 # f.readlines() - 데이터를 리스트형태로 라인별로 담아준다
fr.close()

rw= open("tips_copy.csv", "w", encoding="UTF-8")
lista = []
listb = []
rw.write(lines[0])
for a in range(1, 245):
    lista.append(lines[a])
for b in lista:
    listb.append(b.split(','))
for a in listb:
    a[-1] = a[-1].replace('\n','')
    a.append(str(float(a[1])/float(a[0])*100)+"%\n")
    a = ','.join(a)
    rw.write(a)
rw.close()



# f = open("tips.csv", "a", encoding="UTF-8")
# for i in range(2, 245):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()

