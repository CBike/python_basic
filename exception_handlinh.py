try:
    print(" 나누기 전용 계산기 ")
    nums = []
    nums.append(int(input("첫번쨰 숫자를 입력 하세요 :")))
    nums.append(int(input("두번쨰 숫자를 입력 하세요 :")))
    # nums.append(int(nums[0]/nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

