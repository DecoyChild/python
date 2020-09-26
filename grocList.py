'''
Shayne Greene
IT-140
Grocery List
Users input and item, item quantity and price. Items are stored in a dictionary and added
to a list. All items are then calculated and printed to the screen
9/26/20
A.3
'''

#Empty Dictionary and list 
grocery_item = {}

grocery_history = []

#Variable for total
grand_total = 0

#check variable for loop
stop = 'c'

#Loop for user inputs
while stop == 'c':
  
  #imput prompts for item
  item_name = input('Item name:\n')
  
  quantity = input('Quantity purchased:\n')
  
  cost = input('Price per item:\n')
  
  #adding items to dictionary
  grocery_item.update({'name' : item_name})
  grocery_item.update({'number' : quantity})
  grocery_item.update({'price' : cost})
  
  #creating a copy of the dictionary to append to the list
  grocery_item_copy = grocery_item.copy()

  #adding grocery item to list
  grocery_history.append(grocery_item_copy)
  
  #prompts for input on continue or quit
  stop = input('Would  you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')

#loop calculates item price and outputs to screen and adds to grand total
for item in grocery_history:
  
  item_total = int(item['number']) * float(item['price'])

  grand_total += item_total

  print(str(item['number']) + ' ' + item['name'] + ' @ $' + "{:.2f}".format(float(item['price'])) +
       ' ea $' + "{:.2f}".format(float(item_total)))
  
  item_total = 0

#displays grand total
print('Grand total: $' + "{:.2f}".format(grand_total))