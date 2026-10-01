withdrawal_amount = int (input("Enter the required amount"))
balance = int (input("Enter the balance amount"))
if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount > balance:
    print("Insuffient bank balance")
elif withdrawal_amount % 100 == 0:
    print("Withdrawal successful")
    print("Remaining balance: ",balance-withdrawal_amount)
else:
    print("Amount should be in multiples of 100")