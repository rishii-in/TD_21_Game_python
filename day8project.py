import random

truths = [
    "What is your biggest fear?",
    "Who is your secret crush?",
    "What is your most embarrassing moment?",
    "Have you ever lied to your best friend?",
    "What is a secret no one knows about you?",
    "What is your worst habit?",
    "What is the strangest dream you've had?",
    "Who do you like the most in me ?",
    "Who do u hate the most and why ?",
    "What is your biggest regret?",
    "What is something you are afraid to tell your parents?",
    "Who was your first crush?",
    "What is the most childish thing you still do?",
    "What is your biggest insecurity?",
    "What is one thing you would change about yourself?",
    "Have you ever stalked someone on social media?",
    "What is the weirdest thing you have eaten?",
    "What is your guilty incident you need to overcome some day ?",
    "Have you ever been rejected?",
    "What is your biggest lie?"
]

dares = [
    "Treat me any food with 50 rupees 💪",
    " send me any singing video 🎤",
    "call your crush or msg 'hi' 💃",
    " Propose me  🐒",
    "Talk in a flirty accent for 1 minute 😆",
    "say your fav actor dialogue 🎭",
    "Send me ur current pic 😝",
    "send me any singing video 🚶",
    "Show me your chrome and google and yt history 👶",
    " Call your friend and instead of calling there name , call some other person name they hate 🏃",
    "Keep a story that will definetly affect your friends and ask about that  😜",
    " Call your enemy and say i like you 😂",
    " Dont use instagram for 1 day 🦸",
    " Talk to any starnger randomly in college like u know them before 😵",
    " Try any weirdest combo of food and review it 🤐",
    " DO a prank that u love some one 💗",
    " Call ur bestie and say i hate u 🤐 ",
    " Dance for ur fav song atleast a step  😝",
    " Dont eat outside food for a Day 🐶",
    " Watch a horror movie at 12pm  🔥"
]

print("----------🎮 Welcome  to TD_21 Game 🎮------------ ")

while True:
    num=0

    input("\nPress enter to start the game....")
    print()
    print("---------Choosing number from 1 to 21 🔢------- ")

    while True:
        comp=random.randint(1,3)
        print()
        print("\n🤖 Computer Turn :")
        for i in range(comp):
            num+=1
            print(num,end=" ")
            if num==21:
                print("🎉 You Win !! computer lost 😎")
                break
        if num==21:
            break
        print()
        print("\nYour Turn:")
        user=input("enter your numbers(1-3):")

        if not user.isdigit():
            print("Enter valid number ❌ ")
            continue

        user=int(user)

        if user<1 or user>3:
            print("Choose in range of (1-3)")
            continue
        
        for i in range(user):
            num+=1
            print(num,end=" ")
            
            if num==21:
                print()
                print("\n💀 You Lose")
                print("Choose any one ")
                print("1.Truth 🤔")
                print("2.Dare 😈")
             
                while True:
                    td=input("\nenter your choice (1 or 2 ) :")
                    print()
                    if not td.isdigit():
                        print("Invalid choice ❌")
                        continue
                
                    td=int(td)
                
                    if td==1:
                        print(random.choice(truths))
                        break
             
                    elif td==2:
                        print(random.choice(dares))
                        break

                    else:
                        print("⚠️ Enter number ( 1 or 2 ) : ")
                

        if num==21:
            break
    
    print("\n🎭 Truth/Dare completed!\n")
    choice=input("Do you want to play again(Yes,No):").upper()
    if choice!="YES":
            print("\n 👋see you again ... Thanks for playing 💗 !!")
            break
