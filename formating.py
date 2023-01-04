#case1 %

print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % '파이썬')
print("나는 %c살입니다." % 'A')
print("나는 %s살입니다." % 22)

print("나는 %s 색과 %s색을 좋아해요"% ("파랑","빨강"))

#case2
print("나는 {}살 입니다.".format(20))
print("나는 {}살 입니다.".format(20))
print("나는 {1}살 {0} 입니다.".format(20, 21))
print("나는 {0}살 {1} 입니다.".format(20, 22))

#case3
print("나는 {age} 살이며, {color} 색을 좋아해요.".format(age = 20, color = "red"))
print("나는 {color} 살이며, {age} 색을 좋아해요.".format(age = 20, color = "red"))

#case4 python 3.6 이상

age = 20
color = "빨강"
print(f"나는 {color} 살이며, {age} 색을 좋아해요.")
