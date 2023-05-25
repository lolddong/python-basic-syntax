# tuple은 변경불가능한 자료형으로서 ()로 표현
    # 예) t1 = (1, 2, 'a', 'b', [1, 2, 3])
# 조회하는 인덱싱, 슬라이싱 등은 list와 동일하게 가능
# 변경하는 삭제, 변경, 추가, 수정 등은 불가
    # del t1[1]
    # >> TypeError: 'tuple' object doesn't support item deletion
# 신규로 만드는 더하기, 곱하기 가능
    # t1 = (1, 2, 3)
    # t2 = ('a', 'b', 'c')
    # t3 = (t1 + t2)
    # print(t3)
    # >>
# 사용 목적:
    # 불변값 사용시 메모리 효율적: 개발자가 해당 자료를 수정하지 못하도록 강제적으로 지정한 것
    # list에 비해 메모리 효율적

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t3 = (t1 + t2)
print(t3)
