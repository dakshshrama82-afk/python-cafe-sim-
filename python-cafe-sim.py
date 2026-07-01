#asking the client info and giving the menu

print("Hello! Welcome to our café. My name is Aman, and I'll take your order today.")
clinte_name = input("May I know your name, please?:")
Titel = input("May I kindly ask how you would like to be addressed (Mr., Mrs.,etc)")
print(Titel,clinte_name ,"Here is our menu.What would you like to have today?")


menu = {
    "Coffee": 120,
    "Tea": 80,
    "Sandwich": 150,
    "Cake": 200,
    "Juice": 100,
}
print( menu )

order = input("please enter the item you would like to order from the menu:")
quantity = int(input("how manny would you like to order"))
prise = menu[order]
sum = prise* quantity

print("Thank you for your order, ", Titel, clinte_name, ". Your total bill is: Rs.", sum)
