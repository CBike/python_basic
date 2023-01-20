"""
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동주문 시스템을 제작 하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

조건 1: 1보다 작거나 숫자가 아닌 입력갑이 들어올 때는 ValueError 로 처리
        출력 매세지 : "잘못된 값을 입력 하였습니다."

조건 2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : " 재고가 소진 되어 더 이상 주문을 받지 않습니다."

"""
class SoldOutError(Exception):
    def __init__(self, msg):
        self. msg = msg

    def __str__(self):
        return self.msg


chicken = 10
waiting = 1
while True:
    try:
        print(f"남은 치킨 : {chicken}")
        order = int(input("치킨 몇 마리 주문 하시겠습니까?"))
        if order < 1:
            raise ValueError
        if order > chicken:
            print("재료가 부족 합니다.")
        else:
            print(f"대기 번호 {waiting} {chicken}마리 주문이 완료되었습니다.")
            waiting += 1
            chicken -= order
            if chicken <= 0:
                raise SoldOutError("재고가 소진 되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
        print("잘못된 값을 입력 하였습니다.")
    except SoldOutError as e:
        print(e)
        break