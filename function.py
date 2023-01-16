def open_account():
    print("새로운 계좌가 생성 되었습니다.")

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money} 입니다.")
    return balance + money

if __name__ == '__main__':
    open_account()
    balance = deposit(500000000,1000000)
