#Q.1- Create a list with user defined inputs. 

l1=[]
choice='y'
while choice=='y':
	element=input("Enter something to be added in list: ")
	l1.append(element)
	choice=input("Do you want to enter more? y/n: ")
print(l1)
