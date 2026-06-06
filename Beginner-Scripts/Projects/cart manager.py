
# products in cart
Cart = ['Turkey', 'Orange']
# Adds watermelon, mango and Bananas in the cart
Cart.append('Watermelon')
Cart.append('Mango')
Cart.append('Banana')
print(Cart)
# removes Orange from cart
Cart.pop(1)
# Buys Turkey
bought_items = Cart.pop(0)
print(f'checked out item:' , bought_items)
# rest of Items remain in cart 
print(f'Remaining in cart:' , Cart)
