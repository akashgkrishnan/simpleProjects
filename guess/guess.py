from random import randint
print("*"*30)
print("****Guessing Game****")
print("*"*30)
ch = 'y'
count = 0
while ch == 'y':
    ran = randint(1,10)
    print(f"ran = {ran}")
    num = int(input("Enter a random number between 1 and 10: lets see if you can guess what the computer is thinking: "))
    count += 1

    if num == ran:
        print(f"Yay!! Nice guessing. You and the computer Guessed {num} it took you {count} number of attempts")
        ch = input("Do you want to continue (y/n): ").lower()
        count = 0
    else:
        print("Nah!! Bad guess")
        ch = input("Do you want to continue (y/n): ").lower()





