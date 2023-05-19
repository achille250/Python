#enter an item name and price
shopping_cart_list=[]

while True:
    name=input('Enter the name of item or "done" to finish')
    if name =='done':
        break
    price=input('Enter the price"or "done" to finish')
    if price=='done':
         break

    shopping_cart_list.append(name)
    shopping_cart_list.append(price)

print(shopping_cart_list)

item_to_remove=input("Enter the name you want to remove in shopping_cart")
if item_to_remove in shopping_cart_list:
     shopping_cart_list.remove(item_to_remove)
     print ("this item has been removed",item_to_remove)
else:
   print ("this item doesn't exist",item_to_remove)
print (shopping_cart_list)