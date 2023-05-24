# 이 #표시는 프로그래밍에서 주석이라 말한다.
# 주석은 파이썬의 인터프이터가 인식하지 못하도록 쓰는 기호
# 단축키는 Ctrl + /

# 아래 a = 1 의 의미는 a와 1이 같다라는 의미가 아니라,
# a라는 이름의 변수에 1을 담겠다는 뜻이다.
# a = 1
# b = '1'

# print는 실행 후 결과값을 가시적으로 보여주기 위해 터미널 창에 출력하는 것
# print(a)
# print(b)

# 아래 뜻은 '새로운 a' 값에 "'원래 a' 값 더하기 1" 값을 넣겠다는 뜻이다
# a = a + 1
# print(a)

# 변수 자료형 출력해보기  
# a = 1
# b = True
# c = 2.3
# print(type(a))
# print(type(b))
# print(type(c))

# 문자 자료형 출력해보기
# x = "a"
# print(ord(x))
# >> 97
# y = "A"
# print(ord(y))
# >> 65

# multi line으로 문자열을 표현하고 싶으면 쌍따음표/홑따음표 3개를 사용하면 된다.
# a = """hello

# world"""
# print(a)

#그렇다면 python's easy 라는 문구를 출력해보자
# a = "python's easy"
# print(a)

# 이스케이프문을 활용한 줄바꿈
# 이스케이프문이란 \n (줄바꿈) 또는 \t (tap키) 등의 특수기호를 말한다.
# a = "hello\nworld"
# print(a)
# a = "hello\tworld"
# print(a)
# \역슬래시(won doller 포함)의 또다른 활용: 특수문자를 있는 그내로 표현하는 역할
# "쌍따음표("")는 파이썬에서 문자를 의미한다"라는 문구를 출력해보세요.
# a = "쌍따음표(\")는 파이썬에서 문자를 의미한다"
# print(a)
# a라는 변수에 python이라는 문자열을 담고, 
# b 라는 변수에 is hun이라는 문자열을 담는다.
# 그리고 cf라는 변수에 두 문자열을 더한 값을 넣어 c를 출력
# a = " python "
# b = " is fun "
# c = a + b
# print(c)

# 문자열 곱하기
# python python is fun 이라는 문자욜를 c에 담아 출력
# c = a * 2 + b
# print(c)

# 문자 h를 출력하라
# a = "python's fun"
# print(a[3])

# 문자열의 마지막문자를 출력해보자
# a = "python's fun python's fun python's fun"
# print(a[-1])

# 문자열의 길이를 구하는 함수는 len()
# print(a[len(a)-1])

# 문자열의 슬라이싱: 슬라이싱이란 문자열을 잘라내는 것

# 대상변수[x:y] -> x이상 y미만의 index를 가진 문자열을 잘라낸다
a = "python is fun"
# python만 잘라내서 b에 담아 출력
# b = a[0:6]
# print(b)
# >> python
# x, y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# 6번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력
b = a[6:]
print(b)
# 

# a[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고
# 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
# print(a[2:7:2])

# 연습문제(슬라이싱)
# a = '20220505children's_day' 슬라이싱을 이용하여 date라는 변수에 날짜, day라는 변수에 children's_day을 담아서 각각 출력(print)
# a = '20220505children\'s_day'
# date = a[0:8]
# day = a[8:]
# print(date)
# print(day)

# 문자열 포맷팅

# 문자열 포맷팅이란 문자열 중간에 특정 문자 (또는 숫자 등)를 삽입하는 방식
# 포맷팅 쓰는 이유: 문자열을 직접 삽입하면 1회성으로 coding할 수 박에 없지만, 포맷팅은 변수값을 삽입할 수 있다; 따움표를 여러번 안 닫아도 된다
# %s: 문자열, %d: 정수 (d = digit), %f: 실수
# 함수 input() 의 값은 항상 str(문자) 값이 된다; 그러므로 %d나 %f로 형변화 시켜줘야 된다 -> int() 아니면 float()
# language = input("좋아하는 언어를 입력하세요.")
# times = input("그 언어를 몇 번이나 공부하셨나요?")
# a = "I studeid %s very hard %d times." % (language, int(times))
# print(a)

# 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이 해서 귀찮다
# a = "I studied " + language + " very hard " + times + " times."
# print(a)

# 연습문제
# 나이가 몇 살이신가요? 해서 나이를 받고, 몸무게가 몇 킬로그램이신가요? 해서 weight 받고, My age is %d, and weight is %f kg
# 위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고 그 결과값을 출력
# age = input("나이가 몇 살이신가요?")
# age = int(input("나이가 몇 살이신가요?")) <- 여기다가 정수변환 해도 됨
# weight = input("몸무게가 몇 킬로그램이신가요?")
# weight = float(input("몸무게가 몇 킬로그램이신가요?")) <- 여기다가 실수변환 해도 됨
# a = "My age is %d, and weight is %f kg." % (int(age), float(weight))
# print(a)

# 문자열 관련 주요 함수
# count: 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# a = "python"
# print(a.count('o'))
# find: 대상 문자열에서 지정한 문자가 몇 번째 index에 있는지 출력하는 함수
# index: find와 같은 기능
# print(a.find('o'))
# print(a.index('o'))
# 없는 문자를 찾을 때에는 -1 return한다
# print(a.find('x'))

# whatyouwant = input("아무런 문자나 입혁해주세요")
# search = input("찾고자 하는 문자 1개만 입력해주세요")
# result = whatyouwant.find(search)
# if result == -1:
    # print("찾고자 하는 값이 없습니다.")
# else:
    # print("요청하신 문자는 %d 번째에 있습니다." % result)

# 대소문자 변경: upper() / lower()
# a = "hello"
# print(a.upper())
# b = "HELLO"
# print(a.lower())

# 문자열 양쪽 공백을 없애는 함수: strip()
# a = "     hello world      "
# print(a.strip())

# myId = (input("id를 입력해주세요")).strip()
# myPw = input("비밀번호를 입력해주세요")
# print("ID는 " + myId + "이고 " + "비밀번호는 " + myPw + "입니다.")

# 문자열 대체: replace()
# a = "I studied python"
# print(a.replace("python", "java"))
# print(a.replace("I", "My friend"))

# 문자열 쪼개기 / 공백을 기준으로 문자를 자르는 함수: split()
# a = "I studied python."
# b = a.split(" ")
# print(b)
# >> ['I', 'studied', 'python.']

# a = "I     studied      python."
# b = a.split(" ")
# c = a.split()
# print(b) 
# >> ['I', '', '', '', '', 'studied', '', '', '', '', '', 'python.']
# print(c) 
# >> ['I', 'studied', 'python.']

# a = "I:studied:python."
# b = a.split(":")
# print(b) 
# >> ['I', 'studied', 'python.']

# 연습문제(숫자형)_교제
# 아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력
# y = 2.5 * x^2 + 3.3 * x + 6
# 출력화면
# x = int(input("x값을 입력해주세요"))
# y = 2.5 * pow(x, 2) + 3.3 * x + 6
# print(y)

# 3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력
# <조건1> 각 단어 변수 (word1, word2, word3)
# <조건2> 입력과 출력 구분선: 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
# word1 = input("첫번째 단어를 입력해주세요.")
# word2 = input("두번째 단어를 입력해주세요.")
# word3 = input("세번째 단어를 입력해주세요.")
# print(word1[0] + word2[0] + word3[0]) 
# >> Korea, Busan, Kangnam 라고 입력했을 때 >> KBK