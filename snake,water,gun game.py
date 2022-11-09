import random
def swg(comp,mine):
    if comp==mine:
        return None
    if comp=="w" and mine=="s":
        return True
    elif comp=="s" and mine=="g":
        return True
    elif comp=="g" and mine=="w":
        return True
    else:
        return False    

choice=("s","w","g")
comp=random.randint(0,2)
comp=choice[comp]
mine=input("Enter the s,w or g: ")
win=swg(comp,mine)
if win is None:
    print(f"You choose {mine} and my comp choose{comp}")
    print("Draw")
if win:
    print(f"You choose {mine} and my comp choose{comp}")
    print("I won")
else:
    print(f"You choose {mine} and my comp choose{comp}")
    print("I loose")
