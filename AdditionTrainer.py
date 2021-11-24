import random
score = 0
score = int(score)


name = input("What is your name? ")
name = name.title()
print("""Hello {}, You will be presented with 10 questions.
Enter the appropriate answer to each question. Good luck!""".format(name))
print("\n")

#item1
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("1. ", str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item2
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("2. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item3
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("3. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item4
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("4. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item5
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("5. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item6
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("6. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item7
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("7. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item8
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("8. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item9
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("9. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")
    
print("Your current score is " + str(score) + " out of 10")

#item10
addend1 = random.randint(0,99)
addend2 = random.randint(0,99)
print("10. ",str(addend1), "+", str(addend2), "= ?")
answer1 = int(input("Your answer is:"))

if(addend1 + addend2 == answer1):
    print("Well done! that is correct!")
    score = score + 1
else:
    print("Sorry, that is not correct")

print("Your total score is " + str(score) + " out of 10")
print("Thank you for playing {}, goodbye!".format(name))