def list():
	remainder=[number/3 for number in range(100,150)]
	print(remainder)

def sort():
	a=["apple","banana","mango"]
	b=["avocado","peach","orange"]
	c=["pineapple","lemon"]
	d=[]
	d=a+b+c
	d.sort()
	print(d)


def divisible_by_three(n):
	range_num=range(1,n-1)
	final_num=(range_num)/3
	print (final_num)


def flatten():
	x=[[1,2],[3,4],[5,6]]
	flatten.append(x)
	print(x)



def smallest():
	list=[1,3,6,8,2,4,5.7]
	print(min(list))


def remove():
	x = ['a','b','a','e','d','b','c','e','f','g','h']
	x.pull()
	print(x)


def squares():
	a=dict()
	numbers=range(149,159)
	for number in numbers:
		a[number]=number**2
		print(a)


def students():
	Student1={"age":19,"name":"Eunice"}
	Student2={"age":21,"name":"Agnes"}
	Student3={"age":18,"name":"Teresa"}
	Student4={"age":22,"name":"Asha"}

	Students=[Student1,Student2,Student3,Student4]

	for Student in Students:
		print("Hello {},you were born in year {}.".format(Student["name"],Student (2019-["age"])))