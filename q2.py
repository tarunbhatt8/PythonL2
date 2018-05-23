''' Q.2- Add the following list to above created list(list created in q1):
['google','apple','facebook','microsoft','tesla'] '''

l1=[]
choice='y'
while choice=='y':
	element=input("Enter something to be added in list: ")
	l1.append(element)
	choice=input("Do you want to enter more? y/n: ")
print(l1)

l2=['google','apple','facebook','microsoft','tesla']

l1.extend(l2)
print(l1)
