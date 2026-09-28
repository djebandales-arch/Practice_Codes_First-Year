#Bus Fare Calculator
print("\n-----------BUS FARE------------")
age = int(input("How old are you? --> "))
is_student = bool(input("Are you a student? --> "))
distance = int(input("Input your distance? --> "))
has_pass = bool(input("Do you have a pass? --> "))

fare = distance * 1.5

#outer
if age >= 5:
    print("Accepted: \nAllowed to ride")
    if age < 12:
        fare *= 0.5 #half price
        print("Your fare is halved, your fare is now", fare)
    elif age >= 60:
        fare *= 0.7 #senior discount
        print("You have a senior citizen discount, you fare is now", fare)
    if is_student == True:
        fare -= 2.0
        print("Student discount is applied, your fare is now", fare)
    if has_pass == True:
        fare = 0.0
        print("You have a pass so your fare is now", fare)
else:
    print("Rejected: \nToo young to ride alone")

print("\n=====ABC COMPANY TICKET=====" )
print("Age: ", age)
print("Student: ", is_student)
print("Distance: ", distance)
print("Has Pass", has_pass)
print('Total Fare', fare + fare)