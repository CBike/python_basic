# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print(name, age, end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
def profile(name, age, *language):
    print(name, age, end=" ")
    for lang in language:
        print(lang,end="")
    print()

profile("유재석",20,"파이썬","자바","C#","C++","C")
profile("김태호",20,"코틀린","스위프트")

