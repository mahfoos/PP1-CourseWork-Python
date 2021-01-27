# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
# Any code taken from other sources is refeenced within my code solution.

# Student ID:20191191

# UoW ID:W1790335

# Last Updated date:16.04.2020

progress,trailing,retriever,excluded = 0,0,0,0

def histogram():
    global progress,trailing,retriever,excluded 
    print("--------Vertical Histogram--------")
    print("Progress","Trailing","Retriever","Excluded")
    while progress + trailing + retriever + excluded != 0:
        if progress !=0:
            print("\t",end=" ")
            progress -= 1
        else:
            print("        ",end="")
            
        if trailing!= 0:
            print("    *   ",end=" ")
            trailing -= 1
        else:
            print("        ",end="")
            
        if retriever != 0:
            print("    *   ",end=" ")
            retriever -= 1 
        else:
            print("        ",end="")
            
        if excluded  != 0:
            print("    *   ",end=" ")
            excluded  -= 1
        else:
            print("        ",end="")
        

def check(values):
    try:
        user_input = int(input(values))

        if 120 >= user_input >= 0 and user_input % 20 == 0: # check the range 
            return user_input

        else:
            print("Range error")

    except ValueError:
        print("Integer Required ")

    return check(values)


def condition():
    global progress,trailing,retriever,excluded
    pass_credit = check("Enter the pass credit:")
    defer_credit = check("Enter the defer credit:")
    fail_credit = check("Enter the fail credit:")
    total = pass_credit + defer_credit + fail_credit
    if total != 120:
        print("Total incorrect")
        condition()
        
    elif pass_credit == 120:
        print("Progress")
        progress += 1  # count the progress
        
    elif pass_credit == 100:
        print("Progress -module trailer")
        trailing += 1  # count the module trailer
        
    elif pass_credit + defer_credit >= 60:
        print("Do not progress -module retriever")
        retriever += 1 # count the moule retriever
        
    else:
        print("Exclude")
        excluded += 1  # count the exclude

def choice():
    while True:
        condition()
        
        start = input("\nPress any key to continue the program \nPrss 'Q' to Display the histogram and quit the program\n")
           
        if start.lower() == "q":
            histogram()
            break # after display the histogram program is stop
        
      

      


choice() # call the function to start the program
