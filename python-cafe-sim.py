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

order = input("please enter the item you would like to order from the menu:")
if order != menu:
    print("we do not have that item in our menu. Please choose an item from the menu.")

add_item = input("would you like to add any other item to your order? (yes/no):")
if add_item== "yes":
    order2 = input("please enter the item you would like to order from the menu:")
else:
    print("Thank you for your order. We will prepare it for you.")

  

quantity = int(input("how manny would you like to order"))
prise = menu[order] + menu[order2]
sum = prise* quantity

print("Thank you for your order, ", Titel, clinte_name, ". Your total bill is: Rs.", sum)
