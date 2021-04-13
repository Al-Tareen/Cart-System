class Product:
	def __init__(self):
		self._productName = ''
		self._productPrice = ''

	def setProductName(self, productName):
		self._productName = productName
	def getProductName(self):
		return self._productName

	def setProductPrice(self, productPrice):
		self._productPrice = productPrice
	def getProductPrice(self):
		return self._productPrice

	def _calculateSubtotal(cart):
		_subtotal = 0.00 #Starting cart balance
		for item in range (len(cart)):
			_subtotal += cart[item].getProductPrice()
		return _subtotal

	def _calculateTax(cart):
		return (float(Product._calculateSubtotal(cart)) * 0.0825) #Tax rate = 8.25%

	def getTotal(cart):
		return (Product._calculateTax(cart) + Product._calculateSubtotal(cart)) #Would have like to used math module to round-down to 10 decimal place to meet your final answer, but not sure if acceptable. 

	def getReceiptData(cart):
		return Product._calculateSubtotal(cart), Product._calculateTax(cart)