# Nedbank Loan Calculator
print("---Welcome To Nedbank Loan Console Calculator---")

loan_amount = int(input("Please enter loan amount: "))
interest_rate = float(input("Please enter your interest rate without a percentage sign: "))
_number_of_months = float(input("Please enter how many months: "))


if interest_rate <= 7:
    total_repayment = ((interest_rate / 100) * loan_amount * _number_of_months + loan_amount)
    monthly_installment = total_repayment / _number_of_months
    print("The interest rate is smaller than 7 \n")

    print("Monthly installment: ", monthly_installment)
    print('Total Repayment: ', total_repayment, "\n")

    print("Please go to the nearest nedbank branch with you bank statement, ID and proof  of residence.")


if interest_rate >= 24.5:
    total_repayment = ((interest_rate / 100) * loan_amount * _number_of_months + loan_amount)
    monthly_installment = total_repayment / _number_of_months
    print("The interest rate is greater than 24.5 \n")

    print("Monthly installment: ", monthly_installment)
    print('Total Repayment: ', total_repayment, "\n")

    print("Please go to the nearest nedbank branch with you bank statement, ID and proof  of residence.")
