# Angela Alfaro
#Health Insurance Risk Calculator

INTRODUCTION = '''
       ........................................................
                    Health Insurance Calculator 2022
        ........................................................
This calculator is to calculate your risk score. That will be determined by 
the body mass index, blood pressure, age, and family history of disease. Please 
for each question answer with honesty. If not answered honestly will ask you to 
insert response again. 
'''
print(INTRODUCTION)
while True: 
    while True:
                USERSRES1=(input("What is your age?"))
                try:
                    USERSRES1=int(USERSRES1)
                except:
                    print("Enter the correct age.")
                    continue 
                if USERSRES1 <= 0: 
                    print("Please eneter your correct age.")
                    continue
                if USERSRES1 >= 99: 
                    print ("Please enter your correct age.") 
                    continue
                break
    if USERSRES1 > 30:
        points1 = 0
    elif USERSRES1 < 45:
        points1 = 10
    elif USERSRES1 < 60: 
        points1 = 20
    else: 
        points1 = 30
    print("Risk Score: " + str(points1))
    
    while True: 
            USERSRES2= (input("What is your height in INCHES!"))
            try: 
                USERSRES2= int(USERSRES2)
            except:
                print("Please enter your height in INCHES!")
                continue 
            if USERSRES2 <= 0: 
                print ("Please enter the correct HEIGHT!")
                continue
            if USERSRES2 > 90: 
                print("please enter the correct HEIGHT!") 
                continue 
            break
    while True: 
            USERSRES3 = (input("What is your weight in pounds? "))
            try: 
                USERSRES3=int(USERSRES3)
            except: 
                print("Please enter the correct WEIGHT!")
                continue 
            if USERSRES3 < 0: #maybe really skinny 
                print("Please enter the correct weight.")
                continue 
            if USERSRES3 > 450: #extremely overweight 
                print("Please enter the correct weight ")
                continue 
            break
    RawBMI = (USERSRES3 / USERSRES2**2) * 703 
    BMI = round(RawBMI, 1)
    if 18.5<BMI<24.9:
        points2= 0
        print("Normal")
    elif 25<BMI<29.9:
        points2= 30
        print ("overweight")
    else: 
        points2= 75
    print("BMI = " + str(BMI))
    print("Risk Score: " + str(points2))

    while True: 
        USERSRES4 = (input("What is your systolic blood pressure?"))
        try:
            USERSRES4=int(USERSRES4)
        except: 
            print("Please enter a correct systolic blood pressure.")
            continue
        if USERSRES4 < 90: 
            print("Please enter a correct systolic blood pressure.")
            continue 
        if USERSRES4 > 195: 
            print("Please enter a correct systolic blood pressure.")
            continue 
        break
    while True:
        USERSRES5 =  (input("What is yor diastolic blood pressure?"))
        try:
            USERSRES5=int(USERSRES5)
        except: 
            print("Please enter the correct diastolic pressure.")
            continue
        if USERSRES5 < 60: 
            print("Please enter the correct diastolic blood pressure.")
        if USERSRES5 > 140: 
            print("Pleae enter the correct diastolic blood pressure.")
            continue 
        break
    if USERSRES4 < 120 and USERSRES5 < 80: 
        points3 = 0
        print("Normal, Risk Score: " + str(points3)) 
    elif 120 <= USERSRES4 <= 129 and USERSRES5 < 80:
        points3 = 15
        print("Elevated, Risk score: " + str(points3))
    elif 130 <= USERSRES4 <= 140 or 80 <= USERSRES5 <= 89:
        points3 = 30
        print("Stage 1 hypertension, Risk Score: " + str(points3))
    elif 140 < USERSRES4 <= 180 or 90 <= USERSRES5 <= 120:
        points3 = 75
        print("Stage 2 hypertension, Risk Score: " + str(points3))
    elif USERSRES5 > 120: 
        points3 = 100
        print("Emergency, call your primary doctor immediately. Risk Score: " + str(points3))
    elif USERSRES4 > 180:
        points3 = 100
        print("Emergency, call your primary doctor immediately. Risk Score: " + str(points3))

    cancer= input("Do you have a family history of cancer?")
    if cancer == "yes" or cancer == "Yes":
        points4 = 10
        print("Risk Score: " + str(points4)) 
    elif cancer == "no" or cancer =="No": 
        points4= 0
        print("Risk Score: " + str(points4))
    else: 
        print("Please enter in either yes or no.")

    Diabetes = input("Do you have a family history of Diabetes?")
    if Diabetes == "yes" or Diabetes == "Yes":
        points5 = 10
        print("Risk Score: " + str(points5))
    elif Diabetes == "no" or Diabetes == "No":
        points5 = 0
        print("Risk Score: " + str(points5))
    else: 
        print("Please enter either yes or no.")
    
    Alzheimers = input("Do you have a family history of Alzheimers?")
    if Alzheimers == "yes" or Alzheimers == "Yes":
        points6 = 10
        print("Risk Score: " + str(points6))
    elif Alzheimers == "no" or Alzheimers == "No":
        points6= 0
        print("Risk Score: " + str(points6))
    else: 
        print("Please enter either yes or no.")

    totalPoints = points1 + points2 + points3 + points4 + points5 + points6
    if totalPoints<= 20:
        risk =("Low Risk")
    elif totalPoints<= 50:
        risk= ("Moderate Risk")
    elif totalPoints<= 75: 
        risk =("High Risk")
    else: 
        risk = ("uninsurable") 
    print("Your total Risk Score is: " + str(totalPoints) + " You are: " + risk)

    while True:
        res = (input("Want to retry again? (y/n): "))
        if res == "y":
            break 
        if res == "n":
            quit()



            

                    







            
