
import random
options=("rock","paper","scissors")
user_score=0
Computer_score=0
playing=True
while playing:
    user=None
    Computer=random.choice(options)
    while user not in options:
        user=input("choose one from (🪨  rock , 🗞️  paper , ✂️  scissors): ").lower()
        print(f"💻  chose: {Computer}")

    if Computer==user:
        print("🤝 It's a tie!")
    elif user=="rock" and Computer=="scissors":
        print("you win! 🎉")
        user_score+=1
    elif user=="paper" and Computer=="rock":
        print("you win! 🎉")
        user_score+=1
    elif user=="scissors" and Computer=="paper":
        print("you win! 🎉")
        user_score+=1
    else:
        print("you lose! ☹️")
        Computer_score+=1
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ("y", "n"):
            break
        print("Invalid input! Please enter 'y' to continue or 'n' to exit.")

    if play_again == "n":
        playing = False
print("-----------score------------------")
print(f"user_score 👨: {user_score}")
print(f"Computer_score 💻: {Computer_score}")
print("------------result----------------")
if user_score > Computer_score:
    print("👨 user win! 🎉")
elif user_score==Computer_score:
    print("🤝 It's a tie!")
else:
    print("💻 Computer Wins! 🎉")
print("----------------------------------")
print("thanks for playing 💛")

