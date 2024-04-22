rid = ["what belongs to you, but other peopel ues?",
       "what do you brake before using it?", "what is brown and sticky"]


ans = ["you name", " an egg", "a stick"]

def riddle(choice):
    quseton = rid[choice]
    print(quseton)
    answer = input()

    correct = ans[choice]

    while answer != correct:
        answer = input("try again: ")

    print("good job")
