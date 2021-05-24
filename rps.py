import random
import time

def main():
    you, comp = 0, 0
    tup = (1, 2, 3)
    print("Welcome to rock, paper, and scissors.")
    print("After 'Shoot!' please enter in '1', '2', or '3' for rock, paper, and scissors, respectively.")
    while(True):
        print("ROCK!")
        time.sleep(1)
        print("PAPER!")
        time.sleep(1)
        print("SCISSORS!")
        time.sleep(1)
        choice = input("SHOOT!")
        rand = random.choice(tup)
        print("Computer Choice: " + str(rand))
        if choice == 1 and rand == 2:
            comp+=1
        elif choice == 1 and rand == 3:
            you+=1
        elif choice == 2 and rand == 1:
            you+=1
        elif choice == 2 and rand == 3:
            comp+=1
        elif choice == 3 and rand == 1:
            comp+=1
        elif choice == 3 and rand == 2:
            you+=1
        elif choice == rand:
            print("...")
            continue
        print("Your Score: " + str(you) + "\nRobot Score: " + str(comp))
        if you == 3:
            print("YOU WIN!")
            return False
        if comp == 3:
            print("YOU LOSE!")
            return False

if __name__ == "__main__":
    main()
