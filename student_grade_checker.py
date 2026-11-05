print ("Welcome to the program to measure student grades.")
score = float(input ("Enter your grade: \n"))
if score >= 90:
    print ("Excellent")
elif score >= 75:
    print ("Good")
elif score >= 50:
    print ("Pass")
else:
    print("Fail")
