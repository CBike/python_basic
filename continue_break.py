absent = [2,5]
no_book = [7]

for student in range(1,10):

    if student in absent:
        continue
    if student in no_book:
        print(f"오늘 수업 끝이다.{student}번 교무실로 따라와 ")
        break
    print(f"{student}번 책 읽어라")