# import sys
#
# print("python","java","javascript", file=sys.stdout)
# print("python","java","javascript", file=sys.stderr)
#
# scores = {"수학":0,"영어":50,"코딩":100}
#
# for subject, scores in scores.items():
#     print(f"{subject.ljust(8)}는{str(scores).rjust(4)}점 입니다.", sep=":")

#은행 대기 순번표
for number in range(1, 21):
    print("대기번호:"+str(number).zfill(3))


answer = input("아무값이나 입력하세요:")
print(f"입력하신 값은 {answer}입니다.")