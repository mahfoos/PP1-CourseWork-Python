# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
# Any code taken from other sources is refeenced within my code solution.

# W1790335

# 17.04.2020



credits_= ((120,0,0),(100,20,0),(100,0,20),(80,20,20),(60,40,20),(40,40,40),(20,40,60),(20,20,80),(20,0,100),(0,0,120))

progress, trailing , retriever, excluded = 0,0,0,0


def condition():
    global progress , trailing, retriever, excluded
    if pass_credit == 120:
        progress += 1  # counting the progress
        
    elif pass_credit == 100:
        trailing += 1  # counting the module trailer
        
    elif pass_credit + defer_credit >= 60:
        retriever += 1  # counting the moule retriever
        
    else:
        excluded += 1  # counting the exclude


def information():
    print("          Category Outcomes     \n")          
    print("Progress: " ,progress)
    print("Trailing: " ,trailing)
    print("Retriever:" ,retriever)
    print("Excluded: ",excluded,"\n")
    print("          Horizontal Histogram     \n")
    print("Progress: ", progress, progress * "*")
    print("Trailing: ", trailing, trailing * "*")
    print("Retriever:",retriever, retriever * "*")
    print("Excluded: ",  excluded,  excluded* "*")
    print("\nTotal Outcome is 10")
    


index = 0
while index < 10:
    pass_credit = (credits_[index][0])
    defer_credit = (credits_[index][1])
    fail_credit = (credits_[index][2])
    index +=1
    condition()
information()
