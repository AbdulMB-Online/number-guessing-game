# Number Guessing Game
 
A command-line number guessing game written in Python. The computer picks a secret number, and the player tries to guess it within a limited number of attempts. The player can choose between Classic mode and Time Challenge mode, and between three difficulty levels.
 
## Features
 
- **Classic mode:** guess the number within the attempt limit, with no clock.
- **Time Challenge mode:** the same game, but the whole round must finish within 60 seconds. The attempt limit still applies.
- **Three difficulty levels:** each with its own number range and attempt limit.
- **Hints:** after every valid guess the game says "Too high!" or "Too low!" and shows the attempts left.
- **Input validation:** letters, blank entries, and numbers outside the range are rejected without using up an attempt.
## Requirements
 
- Python 3.8 or newer
- No third-party packages (only the `random` and `time` modules from the standard library)
## Setup
 
1. Clone the repository:
```bash
   git clone https://github.com/AbdulMB-Online/number-guessing-game.git
   cd number-guessing-game
```
 
2. (Optional) Create a virtual environment. In PyCharm this is set up when you open the project. From the terminal:
```bash
   python3 -m venv .venv
   source .venv/bin/activate
```
 
   The `.venv` folder is listed in `.gitignore` and is not tracked by Git.
 
## How to Run
 
```bash
python3 guess.py
```
 
## How to Play
 
1. Choose a mode:
```
   1. Classic
   2. Time Challenge
```
 
2. Choose a difficulty:

   | Level | Name   | Range | Attempts |
   |-------|--------|-------|----------|
   | 1     | Easy   | 1-50  | 10       |
   | 2     | Medium | 1-100 | 8        |
   | 3     | Hard   | 1-500 | 10       |
3. Type a number and press Enter. The game tells you whether your guess is too high or too low, and how many attempts you have left.
4. The round ends when you guess the number, run out of attempts, or (in Time Challenge mode) run out of time. When a round ends without a win, the secret number is revealed.
### Time Challenge rules
 
- You have 60 seconds for the whole round, at any difficulty level.
- Before each guess, the game shows the seconds remaining.
- After each valid guess, the game checks the clock. If time has run out, the round ends and the number is revealed, even if that guess was correct.
- `input()` pauses the program, so the game can only notice a timeout after the player presses Enter. This is a known and accepted limitation.
## Settings
 
Settings are named variables at the top of `guess.py`:
 
| Variable       | Default | Purpose                                                              |
|----------------|---------|----------------------------------------------------------------------|
| `TIME_LIMIT`   | `60`    | Seconds allowed for a whole round in Time Challenge mode             |
| `DEBUG_SECRET` | `None`  | When set to a number, forces the secret number so tests are repeatable |
 
Both are for testing only when changed. Set them back to `60` and `None` before committing.
 
## Project Structure
 
```
number-guessing-game/
├── guess.py       # The whole game
├── README.md      # This file, including the test plan
└── .gitignore     # Python gitignore (includes .venv)
```
 
## Git Workflow
 
Each feature was built on its own branch and merged into `main` by pull request:
 
| Branch                      | Feature                            | Merged by |
|-----------------------------|------------------------------------|-----------|
| `feature/classic-mode`      | Classic mode with hints and attempts | PR #1     |
| `feature/difficulty-levels` | Easy, Medium, and Hard levels      | PR #2     |
| `feature/time-challenge`    | Time Challenge mode with 60s limit | PR #3     |
 
## Test Plan
 
| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | Guess that is too low | Easy level, typed a number below the secret (11) | "Too low!" and the attempts left go down by 1 | "Too low!" and "You have 9 attempts left" | Pass |
| 2 | Guess that is too high | Easy level, typed a number above the secret (45) | "Too high!" and the attempts left go down by 1 | "Too high!" and "You have 9 attempts left" | Pass |
| 3 | Correct guess with the right attempt count | Typed the secret number as the very first guess, then won on later guesses in other runs | Win message and a total equal to the number of valid guesses | First version ignored a correct first guess (the win check also required `count` to be non-zero, and 0 counts as false). Fix: removed the extra condition. After the fix the first-guess win reports 1 attempt, and later wins reported 2, 3, 5, 6 and 10 correctly | Pass (after fix) |
| 4 | Letters rejected, attempt count unchanged | Typed `abc` and `v` as guesses | Message shown, asked again, attempts left unchanged | Message shown and asked again. First version printed `<class 'range'>` in the message because it used the wrong variable name. Fix: used my own `ranges` variable. After the fix the message shows the real range | Pass (after fix) |
| 5 | Blank entry rejected, attempt count unchanged | Pressed Enter on an empty guess at 3 attempts left | Message shown, asked again, attempts left unchanged | Message shown. The next wrong guess showed "2 attempts left", so the blank entry did not use an attempt | Pass |
| 6 | Number below the range rejected, attempt count unchanged | Typed `-5` as a guess | "Invalid attempt. Try again." and the attempts left unchanged | First version treated `-5` as "Too low!" and counted it, because I had commented out the range check. Fix: restored the range check as the first branch. After the fix it prints "Invalid attempt. Try again." and the count is unchanged | Pass (after fix) |
| 7 | Number above the range rejected, attempt count unchanged | Typed `999`, `900`, `55` and `221` on different levels | "Invalid attempt. Try again." and the attempts left unchanged | All were rejected with "Invalid attempt. Try again." and the attempt count stayed the same. (`999` first showed "Too high!" before the range check was restored, then passed) | Pass (after fix) |
| 8 | Easy level range and attempt limit | Chose level 1, made a wrong guess | Prompt shows 1 to 50 and 9 attempts left after the first wrong guess | Prompt showed "between 1 and 50" and "9 attempts left" | Pass |
| 9 | Medium level range and attempt limit | Chose level 2, made a wrong guess | Prompt shows 1 to 100 and 7 attempts left after the first wrong guess | Prompt showed "between 1 and 100" and "7 attempts left" | Pass |
| 10 | Hard level range and attempt limit | Chose level 3, typed `900` | Prompt shows 1 to 500, `900` rejected, and 9 attempts left after the first wrong guess | Prompt showed "between 1 and 500" and `900` was rejected. The attempts left after a first wrong guess on Hard still need to be run | Not fully run |
| 11 | Level menu rejects anything else | Typed `4` and `abc` at the level menu, then `1` | Asked again for `4` and `abc`; `1` starts the game | `abc` printed a message and asked again. First version printed nothing for `4`, and a valid choice did not leave the menu loop. Fix: added a message for other numbers and an exit after each valid level. After the fix the menu asks again for bad input and starts the game on `1` | Pass (after fix) |
| 12 | Running out of attempts reveals the number | Easy level, made 10 wrong guesses | Game ends and shows the secret number | "Sorry, you have run out of guesses!! - The secret number was: 42" | Pass |
| 13 | Timeout in Time Challenge reveals the number | Time Challenge with a short limit, waited past it, then typed a valid guess | Game ends with a time-up message and the secret number | First version printed "Time's Up!" but kept asking for guesses. Fix: added an exit to the timeout branch. After the fix the game prints "Time's Up! The secret number was: ..." and ends | Pass (after fix) |
| 14 | Correct guess after time is up still loses | Set a known secret (42), short time limit, waited past it, typed 42 | Time-up message and the number revealed, not a win | "Time's Up! The secret number was: 42" | Pass |
| 15 | Remaining time shown before each guess | Time Challenge, made several guesses | A seconds-left line appears above every guess prompt, including the first | First version never printed the time, then printed it after the guess. Fix: moved the display to the top of the loop, above the guess prompt. After the fix, "Second left: N" appears before every prompt and counts down | Pass (after fix) |
| 16 | Classic mode has no timer | Classic mode, made several guesses | No time lines and no timeout; hints and attempts left still work | A version with an extra `continue` removed hints in Classic mode. Fix: removed it. After the fix there is no timer and the hints work | Pass (after fix) |
| 17 | `DEBUG_SECRET` sets the secret | Set it to 42 and ran the game | The secret is 42; with `None` it is random | First version always overwrote it with a random number. Fix: made the random pick the `else` alternative. After the fix the secret was 42 | Pass (after fix) |
 
## Known Limitations
 
- The timer is only checked after the player presses Enter, because `input()` blocks the program. A real-time cutoff would need threading or similar.
- The game ends after one round. There is no "play again" prompt or score tracking yet.