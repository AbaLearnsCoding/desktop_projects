# collect the necessary input (principal, the annual interest rate, years)
# calculate he monthly payment
# how to the user

def main():
    print("This is a monthly payment loan calculator")
    print("")


    principal = float(input("Input the loan amount: "))
    air = float(input("Input the annual interest rate: "))
    years = int(input("Input the amount of years: "))

    monthly_interest_rate = air/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1+ monthly_interest_rate) ** - (amount_of_months))


    print("Monthly payment of loan is: %.2f" %monthly_payment)

main()
