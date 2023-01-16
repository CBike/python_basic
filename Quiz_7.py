"""
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력 되어야합니다.
- x 주차 주간 보고 -
부서:
이름:
업무 요약 :

1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건 : 파일명은 '1주차.txt','2주차.txt' . . .

"""
weeks = 50
department = '개발 본부'
name = '전양호'
work = '멍때리기'



for i in range(1,weeks+1):
    with open(f'{i}주차.txt','w', encoding='utf8') as report:
        report.write(f"""
        - {i} 주차 주간 보고 -
        부서: {department} 
        이름: {name}
        업무 요약 :{work}
        """)