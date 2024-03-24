# Description: One Stop Insurance Company
# Author: Beth-Ann Penney-Rideout
# Date(s): March 24, 2024

from datetime import datetime 
import FormatValues as FV


# Constants
NXT_POLICY_NUM = 1944
BASIC_PREM = 869.00
DISCOUNT = 0.25
LIAB_COST = 130.00
GLASS_COST = 86.00
LOAN_CAR_COST = 58.00
HST_RATE = 0.15
PROCESS_FEE = 39.99

# Valid provinces
ValidProv = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'NU', 'YT']

# Function for calculating the total premium
def calculate_total_premium(NumCars, ExtraLiab, GlassCover, LoanCar):
    ExtraCost = (NumCars - 1) * (BASIC_PREM * DISCOUNT)
    if ExtraLiab == 'Y':
        ExtraCost += NumCars * LIAB_COST
    if GlassCover == 'Y':
        ExtraCost += NumCars * GLASS_COST
    if LoanCar == 'Y':
        ExtraCost += NumCars * LOAN_CAR_COST
    TotPrem = BASIC_PREM + ExtraCost
    return TotPrem

# Function for calculating the total cost
def calculate_total_cost(TotPrem):
    TotCost = TotPrem + (TotPrem * HST_RATE)
    return TotCost

# Function for calculating the monthly payment
def calculate_monthly_payment(TotCost, DownPmt=None):
    if DownPmt:
        RemainingAmt = TotCost - DownPmt
        MonthlyPmt = (RemainingAmt + PROCESS_FEE) / 8
    else:
        MonthlyPmt = (TotCost + PROCESS_FEE) / 8
    return MonthlyPmt

# Function for displaying claim history
def display_claim_history(Claims):
    print("Claim #  Claim Date  Amount")
    print("-----------------------------")
    for Claim in Claims:
        ClaimNum, ClaimDate, ClaimAmt = Claim
        print(f"{ClaimNum}  {ClaimDate}  ${ClaimAmt:.2f}")

# Main program
def main():
    global NXT_POLICY_NUM
    while True:      # User Information
        FirstNam = input("Enter customer's first name: ")
        LastNam = input("Enter customer's last name: ")
        Add = input("Enter customer's address: ")
        City = input("Enter customer's city: ").title()

        Prov = input("Enter province (2 letters): ").upper()
        while Prov not in ValidProv:
            Prov = input("Invalid province. Please enter a valid 2-letter province: ").upper()

        PostCode = input("Enter customer's postal code (XXX XXX): ")
        PhoneNum = input("Enter customer's phone number(999-999-9999): ")
        NumCars = int(input("Enter the number of cars being insured: "))
        ExtraLiab = input("Extra liability coverage? (Y/N): ").upper()
        GlassCover = input("Glass coverage? (Y/N): ").upper()
        LoanCar = input("Loaner car coverage? (Y/N): ").upper()

        PmtMethod = input("Payment method (Full/Monthly/Down Payment): ").title()
        if PmtMethod == "Down Payment":
            DownPmt = float(input("Enter the amount of the down payment: "))
        else:
            DownPmt = None

        Claims = []
        while True:
            ClaimsNum = input("Enter claim number (or 'done' to finish adding claims): ")
            if ClaimsNum.lower() == 'done':
                break
            ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
            ClaimAmt = float(input("Enter claim amount: "))
            Claims.append((ClaimsNum, ClaimDate, ClaimAmt))

        TotPrem = calculate_total_premium(NumCars, ExtraLiab, GlassCover, LoanCar)
        TotCost = calculate_total_cost(TotPrem)
        MonthlyPmt = calculate_monthly_payment(TotCost, DownPmt)

        # Display Receipt

        print(f"=======================================================================================          ")
        print()
        print(f"                                   One Stop Insurance                                            ")
        print()
        print(f"======================================== Receipt ======================================          ")
        print(f"Policy Number: {NXT_POLICY_NUM}                                                                  ")
        print()
        print(f"Customer Name: {FirstNam.title()} {LastNam.title()}                                              ")
        print(f"Phone Number:  {PhoneNum}                                                                        ")            
        print(f"Address:       {Add}                                                                             ")
        print(f"City:          {City}  Province: {Prov}  Postal Code: {PostCode}                                 ")
        print()
        print(f"Number of Cars:                              {NumCars}                                           ")
        print(f"Extra Liability Coverage:                    {ExtraLiab}                                         ")
        print(f"Glass Coverage:                              {GlassCover}                                        ")
        print(f"Loaner Car Coverage:                         {LoanCar}                                           ")
        print()
        print(f"Payment Method:                              {PmtMethod}                                         ")
        if PmtMethod == "Down Payment":
            print(f"Down Payment:                             {FV.FDollar2(DownPmt):>10}                         ")
        print(f"Total Insurance Premium:                   {FV.FDollar2(TotPrem):>10}                            ")
        print(f"Total Cost (incl. HST):                     {FV.FDollar2(TotCost):>10}                           ")
        print(f"Monthly Payment:                          {FV.FDollar2(MonthlyPmt):>10} (Processing Fee Included)")
        print("\nClaim History:                                                                                  ")
        display_claim_history(Claims)
        print()
        print(f"---------------------------------------------------------------------------------------           ")
        print()
        NXT_POLICY_NUM += 1

        if input("\nDo you want to enter another customer? (Y/N): ").upper() != 'Y':
            break

    print("\nPolicy data has been saved.")

if __name__ == "__main__":
    main()