import random
import time


DEBUG_SECRET = None #For forcing a secret number to test code behaviour
TIME_LIMIT = 60 #No. of seconds for timed mode

#Our main function orchestrating the game
def play_game():
    #Player chooses the mode they want to play
    while True:
        try:
            mode = int(input("1. Classic Mode \n 2. Timed Mode (60s): "))
            if mode in (1, 2):
                break
            print("Invalid Entry. Select a mode between 1 or 2")
        except ValueError:
            print("Invalid Entry. Select a mode between 1 and 2")

    #Player chooses a difficulty level - which further decided no. of attempts and the range of the secret number
    while True:
        try:
            difficulty = int(input("1. Easy - Range:1-50 and Attempts:10 \n""2. Medium - Range:1-100 and Attempts:8 \n""3. Hard - Range:1-500 and Attempts:10 \n "
                                   "Choose a level difficulty between 1 to 3: \n "))
            if difficulty == 1:
                ranges = 50
                attempts =10
                break
            elif difficulty == 2:
                ranges = 100
                attempts = 8
                break
            elif difficulty == 3:
                ranges = 500
                attempts = 10
                break
            else:
                print("Invalid Entry. Select a difficulty level between 1 and 3")
        except ValueError:
            print("Invalid Entry. Select a difficulty level between 1 and 3")

    #the computer generates a random number between 1 and the range decided by the player
    if DEBUG_SECRET:
        num = DEBUG_SECRET
    else:
        num = random.randint(1, ranges)
    count=0 #count keeps the track of number of attempts made by the player
    start_time = time.time() #the clock starts when the game does
    while count < attempts:
        try:
            if mode == 2:
                second_left = max(0,int(TIME_LIMIT-(time.time()-start_time)))
                print(f"Second left: {second_left}")
            #every run users makes an attempt to guess the random number
            guess = int(input(f"Guess a number between 1 and {ranges}: "))
            if guess > ranges or guess < 1: #
                 print("Invalid attempt. Try again.")
            elif mode == 2 and time.time()-start_time > TIME_LIMIT:
                print(f"Time's Up! The secret number was: {num}")
                break
            elif guess == num:
                print("You guessed the number!")
                count += 1
                print(f"You guessed in {count} attempts")
                break
            elif guess > num:
                    print("Too high!")
                    count += 1
                    print(f"You have {attempts - count} attempts left")
            elif guess < num:
                    print("Too low!")
                    count += 1
                    print(f"You have {attempts - count} attempts left")
        except ValueError:
            print(f"Invalid attempt. Try again please enter a number between 1 and {ranges} ")
    else:
        print(f"Sorry, you have run out of guesses!! - The secret number was: {num}")

if __name__ == "__main__":
    play_game()