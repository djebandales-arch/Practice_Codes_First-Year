age = int(input("AGE: "))
monthly_revenue = float(input("MONTHLY REVENUE: "))
credit_score = int(input("CREDIT SCORE: "))
years_in_business = float(input("Years in Business: "))
has_defaults = bool(input("Have you filed for a banckruptcy? "))
collateral_name = str(input("COLLATERAL NAME: "))
collateral_value = float(input("COLLATERAL VALUE: "))

print("============================== \n\tINTERPRETATION\t\t\n==============================\n")


max_lim = 0.0
base_fee = 0.0
tbase_fee = 0
if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("You are eligible for a loan.")
    #tier1
    if credit_score >= 720:
        max_lim = 3 * monthly_revenue
        if monthly_revenue >= 50000:
            base_fee = 0.015
            tbase_fee = max_lim * base_fee
            print("Your loan limit is:", max_lim, "and your base fee is:", tbase_fee)
        else:
            base_fee = 0.025
            tbase_fee = max_lim * base_fee
            print("Your loan limit is:", max_lim, "and your base fee is:", tbase_fee)
        if collateral_value >= max_lim:
                     print("Sufficient loan limit for", collateral_name)
        else:
              print("Insufficient value for", max_lim) 
        if int(collateral_value)%5000 != 0:
              max_lim += 250
              print("You have an additional surgcharge fee of 250 and your base fee is:", tbase_fee + 250)      
        #tier 2
    elif 620 <= credit_score < 720:
            max_lim = 1.5 * monthly_revenue
            if years_in_business >= 5.0:
                max_lim = 1.5 * monthly_revenue
                base_fee = 0.02
                tbase_fee = max_lim * base_fee
                print("Your loan limit is:", max_lim, "and your base fee is:", tbase_fee)
            else:
                max_lim = 1.5 * monthly_revenue
                base_fee = 0.035
                tbase_fee = max_lim * base_fee
                print("Your loan limit is:", max_lim, "and your base fee its:", tbase_fee)
    if collateral_value >= max_lim:
        print("Sufficient loan limit for", collateral_name)
    else:
        print("Insufficient value for", max_lim) 
        if int(collateral_value)%5000 != 0:
            max_lim += 250
            print("You have an additional surgcharge fee of 250 and your base fee is:", tbase_fee + 250)    
        #tier 3
    if credit_score < 620:
         print("Rejected: Credit score below requirement")
else:
    print("Rejected: High Risk Application or Ineligible Owner.")
print("\n\n============================== \n Thank You For Applying! \n==============================\n")