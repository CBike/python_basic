numlist = [5,4,3,2,1]
numlist.sort()
print(numlist)
# 순서 뒤집기 가능
numlist.reverse()
print(numlist)

# 모두 지우기
# numlist.clear()
print(numlist)

# 다양한 자료형 함께 사용

mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장

numlist.extend(mix_list)
print(numlist)