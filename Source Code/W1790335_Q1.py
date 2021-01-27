# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
# Any code taken from other sources is refeenced within my code solution.

# Student ID:20191191

# UoW ID:W1790335

# Last Updated date:16.04.2020


def check(values):
    try:
        user_input = int(input(values))

        if 120 >= user_input >= 0 and user_input % 20 == 0:
            return user_input

        else:
            print("Range error")

    except ValueError:
        print("Integer Required ")

    return check(values)


def condition():
    pass_credit = check("Enter the pass credit:")  
    defer_credit = check("Enter the defer credit:")
    fail_credit = check("Enter the fail credit:")
    total = pass_credit + defer_credit + fail_credit
    if total != 120:
        print("Total incorrect")
        condition()
        
    elif pass_credit == 120:
        print("Progress")

    elif pass_credit == 100:
        print("Progress - module trailer")

    elif pass_credit + defer_credit >= 60:
        print("Do not progress - module retriever")

    else:
        print("Exclude")
        

            
        


condition() # call the function for start the program
