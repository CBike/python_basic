# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,4,5,6,6,6,6,6,6888888888888888889999999}

print(my_set)

java = {"유재석", "김태호", "양세호"}
python  = set(["유재석","박명수"])


#교집합 ( java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))
