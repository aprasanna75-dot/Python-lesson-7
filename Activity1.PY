#Take Input for ths students that he can attend the exam or not
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

#Checking the usre input and predicting output accordingly
if medical_cause =='Y':   #Condition 1
    print("You are allowed")
else:
    # Take input of the attendence
    atten = int(input("Enter the attendence of the students: "))

    if atten >= 75:       #Condition 2
        print("Allowed")
    else:
        print("Not Allowed")