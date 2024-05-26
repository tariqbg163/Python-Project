# This is begineer quiz project
playing = input("Do you want play a quiz >> ")
correct = 0
incorrect = 0

if playing.lower() != "yes":      # if the user enter thing other than yes then quit the program
    quit() # exist the program

answer = input("CPU stands for >> ")
if answer.lower() == "centeral processing unit":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

answer = input("RAM stands for >> ")
if answer.lower() == "random access memory":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

answer = input("ROM stands for >> ")
if answer.lower() == "read only memory":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

answer = input("GPU stands for >> ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

answer = input("OS stands for >> ")
if answer.lower() == "operating system":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

answer = input("DLD stands for >> ")
if answer.lower() == "Digital Logic Design":
    print("Correct!")
    correct +=1
else:
    print("Invalid!")
    incorrect +=1

total_Score = correct + incorrect
correct_Percentage = round((correct/total_Score)*100 , 2)  # round(53.75852, 2) round it to 2 decimal place
incorrect_Percentage = round((incorrect/total_Score) * 100 , 2)


 # round(34.25356433 , 2)  round to 2 decimal place
# print(f"Correct Score = {correct}  ,  { round(((correct/total_Score) * 100),2)}%")  
# print(f"Incorrect = { incorrect} , {round(((incorrect/total_Score) * 100),2)}%") 

print(f"Total Score = {total_Score}")
print(f"Correct Score = { correct } in Percentage = {correct_Percentage}%")
print(f"Incorrect Score = { incorrect} in Percentage = { incorrect_Percentage}%")


if correct_Percentage >= 50:
    print("Wellcome , You pass the quiz!")
else:
    print("Good luck next time!")

# end of project

"""
Things i  covered in this project

1) if statment
2) string.lower() >>>  make the whole string lower
3) upper()  >>>>>>>>> Make the whole string to uppercase
4) capitalize()   >>> Make each first letter of a string capital
"""
