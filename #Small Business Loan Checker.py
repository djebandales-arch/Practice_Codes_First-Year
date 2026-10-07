#Car Rental Shop Eval
renter_age = int(input("AGE: "))
license_years = float(input("HOW MANY YEARS DO YOU HAVE A LICENSE? "))
has_violations = bool(input("HAVE YOU HAD ANY VIOLATIONS? "))
vechicle_class = input("WHAT KIND OF VECHICLE? ")
rental_days = int(input("HOW MANY DAYS ARE YOU GOING TO RENT A CAR? "))
daily_rate = float(input("DAILY RATE: "))

base_cost = 0.0
deposit_rate = 0.0
discount = 0.0
deposit = 0.0             
discounted_cost = 0.0

if renter_age >= 21 and license_years >= 1.0 and has_violations == False:
    print("ACCEPTED: ELIGIUBLE FOR A RENT")
    if rental_days >= 14:
        deposit_rate = 0.10
        base_cost = daily_rate * rental_days
        discount = 0.20
        discounted_cost = base_cost * (1 - discount)
        deposit = discounted_cost * deposit_rate
        if renter_age < 25:
            discounted_cost += 15 * rental_days
            print("You're a young driver, an additional 15$ is added your total is now:", discounted_cost)
        if vechicle_class == "SUV":
            discounted_cost += 50.00
            print("An Additional 50$ is added your total cose is", discounted_cost)
        if rental_days % 2 != 0:
            discounted_cost += 20
            print("An additional 20$ is added your total cost is", discounted_cost) 
            print("Your Total cost is:", discounted_cost, "and deposit is", deposit)
    elif 7<= rental_days < 14:
        deposit_rate = 0.15
        base_cost = daily_rate * rental_days
        discount = 0.10
        discounted_cost = base_cost * (1 - discount)
        deposit = discounted_cost * deposit_rate
        print("Your Total cost is:", discounted_cost, "and deposit is", deposit)
        if renter_age < 25:
            discounted_cost += 15 * rental_days
            print("You're a young driver, an additional 15$ is added your total is now:", discounted_cost)
        if vechicle_class == "SUV":
            discounted_cost += 50.00
            print("An Additional 50$ is added your total cose is", discounted_cost)
        if rental_days % 2 != 0:
            discounted_cost += 20
            print("An additional 20$ is added your total cost is", discounted_cost) 
            print("Your Total cost is:", discounted_cost, "and deposit is", deposit)
    elif rental_days < 7:
        deposit_rate = 0.25
        base_cost = daily_rate * rental_days
        discount = 0.00
        discounted_cost = base_cost * (1 - discount)
        deposit = discounted_cost * deposit_rate
        print("Your Total cost is:", discounted_cost, "and deposit is", deposit)
        if renter_age < 25:
            discounted_cost += 15 * rental_days
            print("You're a young driver, an additional 15$ is added your total is now:", discounted_cost)
        if vechicle_class == "SUV":
            discounted_cost += 50.00
            print("An Additional 50$ is added your total cose is", discounted_cost)
        if rental_days % 2 != 0:
            discounted_cost += 20
            print("An additional 20$ is added your total cost is", discounted_cost)        
else:
    print("REJECTED: INELEGIBLE RENTER:")