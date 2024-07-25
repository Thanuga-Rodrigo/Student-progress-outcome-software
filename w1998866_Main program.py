
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solutions.

# Student ID: w1998866 / 20220599

# Date: 19 April 2023


#Declaring variables
selection = 0
credit_pass = 0
credit_defer = 0
credit_fail = 0
output = 0
list = []
valid = True
file_1 = 0

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
total_count = 0

#user defined functions

#user made function for saving as a text file
def file_save():
    file_1 = open("text_file.txt","w")
    for x in list:
            print(x)
            file_1.write(x + "\n")
    file_1.close()

#user made function for reading what is saven on text file
def read_file():
    file_1 = open("text_file.txt","r")
    content = file_1.read()
    print(content)
    file_1.close()

    
#asking user to input what version do they need        
def menu():
    print("            Main Menu")
    print("-" * 50)
    print("1. Student Version")
    print("2. Staff Verison")
    print("3. Read from Text File")
    print("4. exit")
    print("-" * 50)
      
menu()

while (selection >= 0):
    print()
    selection = int(input("Please indicate your option from main menu - "))
    print()

#option 1 for Student version
    if selection == 1:
        print("Student  Version")
        print()
        while (valid):
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
                    break
                    

        #calculating module trailer

            elif credit_pass == 100:
                    output = "Progress (module trailer)"
                    print(output)
                    print()
                    break
                    
        #calculating exclude

            elif credit_fail >= 80:
                    output = "Exclude"
                    print(output)
                    print()
                    break
                    

        #calculating the module retriever

            elif credit_defer or credit_fail in [0, 20, 40, 60]:
                    output = "Module retriever"
                    print(output)
                    print()
                    break
            continue

                

#option 2 for staff version   
    elif selection == 2:
        print("Staff Version")
        print()
        while (valid):
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
                progress_count = progress_count + 1

        #calculating module trailer

            elif credit_pass == 100:
                output = "Progress (module trailer)"
                print(output)
                print()
                trailer_count = trailer_count + 1
                
        #calculating exclude

            elif credit_fail >= 80:
                output = "Exclude"
                print(output)
                print()
                exclude_count = exclude_count + 1
                
        #calculating the module retriever

            elif credit_defer or credit_fail in [0, 20, 40, 60]:
                output = "Module retriever"
                print(output)
                print()
                retriever_count = retriever_count + 1

        #Part 2 - Making a List and append values to list
                
            inputs_list = output + " - " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail) 
            list.append(inputs_list)
            

        #checking whether user want to con

            
            print("Would you like to enter another set of data? ")
            choice = input("Enter 'y' for yes or 'q' to quit from staff version and view the histogram - ")
            print()
            choice = choice.upper()
            
            if choice == "Y":
                continue

            elif choice == "Q":

        #printing the histogram
                
                print("-" * 60)
                print("Histogram")
                print("Progress", progress_count, ":", "*" * progress_count)
                print("Trailer", trailer_count, ":", "*" * trailer_count)
                print("Retriever", retriever_count, ":", "*" * retriever_count)
                print("Exclude", exclude_count, ":", "*" * exclude_count)
                print()

                total_count = progress_count + trailer_count + retriever_count + exclude_count
                print(total_count, "outcome/s in total")
                print("-" * 60)

                
        #printing the list as output & saving to text file
                print("Part 2:")
                print()
                file_save() #calling user defined function for saving in a text file
                
                break
            
            else:
                print("Invalid letter")

                break

        continue
    
#option 3 for read from the text file
    elif selection == 3:
        print("Contents saved in the text file :")
        print()
        read_file() #calling the user defined function for reading saved text file

        continue

#option 4 for quitting from the program
    elif selection == 4:
        print("End of the program")
        exit()

#if invalid option is given'
    else:
        print("Invalid Option")
        continue

    


