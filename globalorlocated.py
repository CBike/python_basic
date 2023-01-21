gun = 10

def checkpoint(soilders):
    global gun
    gun = gun - soilders
    print("[함수 내] 남은 총 :",gun)

def checkpoint_retrun(gun, soilders):
    gun = gun - soilders
    return gun

def check_porint_out_return():
    pass

print("전체 총 : ",gun)
checkpoint_retrun(gun,2)
print("남은 총 : ",checkpoint_retrun(gun,2))