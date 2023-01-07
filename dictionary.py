cabinet = {3: '유재석', 100:'김태호'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5,"사용 가능"))

print(3 in cabinet)
print(5 in cabinet)
cabinet["C-20"] = "조세호"
cabinet[3] = "김종국"
print(cabinet)

del cabinet[3]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
print(cabinet.clear())
