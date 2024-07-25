#Declaring variables

credit_pass = 0
credit_defer = 0
credit_fail = 0
output = 0
valid = True
dictionary = {}


while (valid):
    student_id = input("Please enter your Student ID including 'w' infront- ")
    print()
    if len(student_id) != 8:
        print("Out of range, Student ID must be 8 characters including 'W'")
        break

    elif student_id in dictionary:
        print("Duplicate Input")
        continue
    
    try:
        credit_pass = int(input("Please enter your credits at pass - "))
        if credit_pass not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range") #checking for out of range input
            print()
            continue
    
        credit_defer = int(input("Please enter your credits at defer - "))
        if credit_defer not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range") #checking for out of range input
            print()
            continue
    
        credit_fail = int(input("Please enter your credits at fail - "))
        if credit_fail not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range") #checking for out of range input
            print()
            continue
        
    except ValueError:   #giving error if integer is not given
        print("Integer Required")
        print()
        continue

#checking whether total of all three equals to 120

    if (credit_pass + credit_defer + credit_fail) != 120:
           print("Total Incorrect")
           print()
           continue

#calculating progress

    if credit_pass == 120:
        output = "Progress"
        print(output)
        print()

#calculating module trailer

    elif credit_pass == 100:
        output = "Progress (module trailer)"
        print(output)
        print()
        
#calculating exclude

    elif credit_fail >= 80:
        output = "Exclude"
        print(output)
        print()
        
#calculating the module retriever

    elif credit_defer or credit_fail in [0, 20, 40, 60]:
        output = "Module retriever"
        print(output)
        print()

#Part 2 - Making a List and append values to list
        
    inputs_list = output + " - " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail) 
    dictionary[student_id] = inputs_list
    

#checking whether user want to continue or end and get the histogram

    print("Would you like to enter another set of data? ")
    choice = input("Enter 'y' for yes or 'q' to quit and view results - ")
    print()
    choice = choice.upper()
    
    if choice == "Y":
        continue

    elif choice == "Q":
         for a,b in dictionary.items():   
                print(f'{a} : {b}')
        
         break