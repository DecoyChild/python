'''
Shayne Greene
ATM Script Draft 9/29/20
Ver. A.2

Script acts as an atm. Allows a customer to deposit, withdraw, and show account balance.
'''
import sys

account_balance = float(500.25)

#Print the account balance
def printbalance():
	print('Your current balance:')
	print(account_balance)

#function to allow deposits
def deposit(account_balance):

	#taking input on the deposit amount 
	deposit_amount = input('How much would you like to deposit today?\n')
	#cast to a float for readability
	deposit_amount = float(deposit_amount) 

	#adding the deposit to the accountBalance
	account_balance += float(deposit_amount)
    
    print('Deposit was $%.2f' % deposit_amount + 
    	', current balance is $%.2f' % account_balance)

#withdraws given amount from account_balance
def withdraw(account_balance):

	#Get withdraw amount from user
	withdrawal_amount = input('How much would you like to withdraw today?\n')
	#cast input to float for readability 
	withdrawal_amount = float(withdrawal_amount) 

	#checks if withdraw is less than account balance, otherwise nothing is updated
	if(withdrawal_amount < account_balance):
		account_balance -= float(withdrawal_amount)

		print('Withdrawal amount was $%.2f' % withdrawal_amount + 
			', current balance is $%.2f' % account_balance)

	else:
		print('$%.2f' % withdrawal_amount + ' is greater than your account balance of $%.2f' 
			% account_balance)


#"menu" portion (would add a while loop to add repeating menu feature)
#Calls functions depending on userChoice  
userChoice = input ("What would you like to do?\n")

if (userChoice == 'D'):
    deposit (account_balance)

elif (userChoice == 'B'):
	printbalance()

elif (userChoice == 'W'):
	withdraw(account_balance)

else:
	print('Thank you for banking with us.')
