print("Welcome to my computer quiz!")

playing = input("Do you want to play this Game? ")

if playing.lower() != "yes":
    quit()
    
print("Okay let's Play:)")
score = 0

answer = input("1] What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("2] What does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("3]What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("4]What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%. ")