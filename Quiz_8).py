"""
주어진 코드를 활용하여 부동산 프로그램을 작성하시오
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

코드

class house
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    def show detail(self):
        pass


"""


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.deal_type} {self.price} ")




m1 = House("강남", "아파트", "매매", "10억", "2010년")
m2 = House("마포", "오피스텔", "전세", "5억", "2007년")
m3 = House("송파", "빌라", "월세", "500/50", "2000년")

m1.show_detail()
m2.show_detail()
m3.show_detail()