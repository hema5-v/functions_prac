#creating a function without parameter 
def func1():
	print("hi")	
func1()	

#function with parameter
def func2(a,b):
	c= a+b
	print(c)
func2(3,6)	

#with default parameter
def func3(university = "iitb"):
	print("i am in"+ "\t" + university)
func3("iitd")
func3("iitg")
func3()	

#calling one function from other
def func4():
	print("hii other func")

def func5():
	print("hello, i am going to call other func")
	func4()	
func5()	

#calling one function from other using parameters
def func4(a,b):
	print("hii other func")
	c = a+b
	print(c)

def func5():
	print("hello, i am going to call other func")
	func4(4,9)
func5()	

#calling one function from other using parameters and return func
def func4(a,b):
	print("hii other func")
	c = a+b
	return c

def func5():
	print("hello, i am going to call other func")
	s = func4(4,9)
	print("addition is",s)
func5()	
		