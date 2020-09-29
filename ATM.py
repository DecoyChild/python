import sys

account_balance = float(500.25)

#printbalance function
def printbalance():
	print('Your current balance:')
	print(float(account_balance))

#deposit function
def deposit(account_balance):
	deposit_amount = input('How much would you like to deposit today?\n')
	deposit_amount = float(deposit_amount)

	#adding the deposit amount to the accountBalance
	account_balance += float(deposit_amount)
    
	print('Deposit was $%.2f' % deposit_amount + 
    	', current balance is $%.2f' % account_balance)


#withdraw function
def withdraw(account_balance):
	#Get withdraw amount from user
	withdrawal_amount = input('How much would you like to withdraw today?\n')
	withdrawal_amount = float(withdrawal_amount) #cast into float for easy fomatting later

	#checks if withdraw is greater than balance
	if(withdrawal_amount < account_balance):
		account_balance -= float(withdrawal_amount)

		print('Withdrawal was $%.2f' % withdrawal_amount + 
			', current balance is $%.2f' % account_balance)

	#FIXMEEEE
	# if withdraw is greater than acct balance --> $700.00 is greater than your account balance of $500.25	
	else:
		print('Withdrawal amount was $%.2f' % withdrawal_amount + ', current balance is $%.2f' 
			% account_balance)

  
userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
    deposit (account_balance)

elif (userchoice == 'B'):
	printbalance()

elif (userchoice == "W"):
	withdraw(account_balance)

#	"{:.2f}".format(float(item_total))