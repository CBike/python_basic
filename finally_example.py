try:
    print("한자리 숫 잔 나눈기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요:"))
    num2 = int(input("두 번째 숫자를 입력하세요:"))

    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print(f"{num1} / {num2} = {num1/num2}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")