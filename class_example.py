class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name}:{location}방향 으로 적군을 공격 합니다.[공격력{self.damage}]")

    def damaged(self,damage):
        print(f"{self.name}:{damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}:현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name}: 파괴 되었습니다.")



marin1 = Unit("마린",40,5)
marin2 = Unit("마린",40,5)
marin3 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

#상속

