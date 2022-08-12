import random
def hangman():
    list=['hangman' , 'debug' , 'kill']
    word =random.choice(list)
    turns=10
    guess_made=''
    entry=set('qwertyuiopasdfghjklzxcvbnm')
    
    while len(word)>0:
        entered_word = ""

        for letter in word:
            if letter in guess_made:
                entered_word+=letter
            else:
                entered_word+="_ "

        if entered_word==word:
            print(entered_word)
            print("YOU WON!!!")
            break
                
        print("Guess a word :",entered_word)
        guess=input()

        if guess in entry:
            guess_made+=guess
        else:
           print("enter valid char")
           guess=input()

        if guess not in word:
            turns-=1


            if turns==9:
                print("9 more turns left!!!")
                print("-------------------")
            if turns==8:
                print("8 more turns left!!!")
                print("-------------------")
                print("         O         ")
            if turns==7:
                print("7 more turns left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")
            if turns==6:
                print("6 more turns left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")
                print("        /        ")
            if turns==5:
                print("5 more turns left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")
                print("        / \        ")
            if turns==4:
                print("4 more turns left!!!")
                print("-------------------")
                print("        \O         ")
                print("         |         ")
                print("        / \        ")
            if turns==3:
                print("3 more turns left!!!")
                print("-------------------")
                print("        \O/        ")
                print("         |         ")
                print("        / \        ")
            if turns==2:
                print("2 more turns left!!!")
                print("-------------------")
                print("        \O/ |      ")
                print("         |         ")
                print("        / \        ")
            if turns==1:
                print("only 1  turns left!!!hangman on danger!!")
                print("-------------------")
                print("        \O/_|      ")
                print("         |         ")
                print("        / \        ")
            if turns==0:
                print("game over!!!")
                
                
name = input("Enter Your Name --- ")
print("WELCOME ",name)
print("--------------------------------")
print("Try to guess word in less than 10 attempts")
hangman()
