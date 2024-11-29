#Multiple values to format method

quantity = 5
item_number = 150
price = 71

neworder = "We Want {} pieces of item number {} and for {:.2f} dollars"
print(neworder.format(quantity,item_number,price))