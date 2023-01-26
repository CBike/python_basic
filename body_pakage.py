#input
language = input("무슨 언어 좋아하세요 ?")
print(f"{language}는 좋은 언어 입니다.")

# dir : 객체를 넘겨줫을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
print(dir())
print(dir(random))
lst = [1,2,3]
print(dir(lst))

# list of python builtins