from Product import Product

p1 = Product()
p1.setProductName("p1")
p1.setProductPrice(5)

p2=Product()
p2.setProductName("p2")
p2.setProductPrice(1)

p3=Product()
p3.setProductName("p3")
p3.setProductPrice(2)

cart = [p1, p2, p3]

subtotal, tax = Product.getReceiptData(cart)

total = Product.getTotal(cart)

#Formatting of Receipt
print("RECEIPT\n")
print("Subtotal: ", '$', subtotal)
print("Tax : ", "$", tax, " (8.25%)")
print("Total Amount Due: ", "$", total)