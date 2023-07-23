import random
isPlay = True
while isPlay == True:  
    

    choice = [1,2,3]

    user = int(input(''' Enter 1 for "Sissor" , Enter 2 for "Paper" , Enter 3 for "Rock" : '''))
    if user == 1:
        user = "Sissor"
    elif user == 2:
        user = "Paper"
    else:
        user = "Rock"
    computer = random.choices(choice)
    if computer == 1:
        computer = "Sissor"
    elif computer == 2:
        computer = "Paper"
    else:
        computer = "Rock"
    print ("user  =  " + user +"   computer = "+ computer)
    if user == computer:
        print ("you won")
    else:
        print("you loss")
    retry = input("Perss enter for replay else anything for quit : ")
    if retry == "":
        isPlay = True
    else:
        isPlay = False

print("Nice to seee you Come Again :) <3  (: )")