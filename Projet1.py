import random


num: int = random.randint(1, 10)
guess:int | None = None
v: str="voiture"
w=5
not_found= num != guess
while not_found:
    guess_str = input("guess a number between 1 and 10: ")
    guess = int(guess_str)
    
    not_found= num != guess
    found = not not_found

    if found:
        print("congratulations! you won!")
        break
    else:
        if guess > num:
            print(f"your number {guess} is too big, try again")
        elif guess < num: 
            print(f"your number {guess} is too small, try again")
        else:
            print("no tapen")    

print("end")
