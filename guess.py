import random

#For classic game we let the user decide the range for guessing
ranges = int(input("Enter the range: "))

#Our main funciton orchestrating the game
def play_game():
    #the computer generates a random number between 1 and the range decided by the player
    num = random.randint(1, ranges)
    count=0 #count keeps the track of number of attempts made by the player
    while True:
        try:
            #every run users makes an attempt to guess the random number
            guess = int(input(f"Guess a number between 1 and {ranges}: "))
            if guess > ranges or guess < 1: #
                 print("Invalid attempt. Try again.")
            elif guess == num:
                print("You guessed the number!")
                count += 1
                print(f"You guessed in {count} attempts")
                break
            elif guess > num:
                print("Too high!")
                count += 1
            elif guess < num:
                print("Too low!")
                count += 1
        except ValueError:
            print(f"Invalid attempt. Try again please enter a number between 1 and {ranges} ")

if __name__ == "__main__":
    play_game()