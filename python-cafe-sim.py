#asking the client info and giving the menu

print("Hello! Welcome to our café. My name is Aman, and I'll take your order today.")
clinte_name = input("May I know your name, please?:")
Titel = input("May I kindly ask how you would like to be addressed (Mr., Mrs.,etc)")
print(Titel,clinte_name ,"Here is our menu.What would you like to have today?")


menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 150,
    "cake": 200,
    "juice": 100,
}
print( menu )

#ordering the item from the menu and checking if the item is in the menu or not

order = input("please enter the item you would like to order from the menu:")
if order in menu:
    quantity = int(input("how many would you like to order"))
else:
    print("we do not have that item in our menu. Please choose an item from the menu.")
    order = input("please enter the item you would like to order from the menu:")
    quantity = int(input("how many would you like to order"))

add_item = input("would you like to add any other item to your order? (yes/no):")
if add_item == "yes":
    order2 = input("please enter the item you would like to order from the menu:")
    if order2 not in menu:
        print("we do not have that item in our menu. Please choose an item from the menu.")
        order2 = input("please enter the item you would like to order from the menu:")
    quantity2 = int(input("how many would you like to order"))
if add_item == "no":
    print("Thank you for your order. We will prepare it for you.")

#taking the quantity of the order and calculating the total bill
if quantity2 > 0:
    totalquantity = quantity + quantity2
else:
    totalquantity = quantity

if order2 in menu:
    totalprise = menu[order] + menu[order2]
else:
    totalprise = menu[order]
sum = totalprise * totalquantity

print("Thank you for your order, ", Titel, clinte_name, ". Your total bill is: Rs.", sum)

#printing the receipt for the order

print("--------cafe receipt--------")
print("Customer Name:", Titel, clinte_name)
print("Order:", order, "and", order2)
print("Quantity:", totalquantity)
print("Total Bill: Rs.", sum)

print("We hope you enjoy your meal! Have a great day!")
