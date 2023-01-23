"""
표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)

여자: 키(m) X 키(m) x22
남자: 키(m) x 키(m) X21

조건 1: 표준 체중은 별도의 함수 내에서 계산
    *함수명: std_weight
    *전달값: 키(height)_성별(gender)
dddddd
조건2: 표준 체중은 소수점 둘째자리까지 표시
출력예제: 키 175cm 남자의 표준 체중은 67.38kg입니다.dddd
"""


def std_weight(height, gender):
    if gender == "man":
        weight = float(height*height* 22)/10000
    else:
        weight = float(height*height* 21)/10000

    print(f"키 {height} {gender}의 표준 체중은 {round(weight,2)}입니다..........................")


std_weight(181,"man")