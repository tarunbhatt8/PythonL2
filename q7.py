#Q.1- Count even and odd numbers in a list.

l1=[]
print("Enter elements of list: ")
ch='y'
while ch=='y':
	element=input('Enter element: ')
	l1.append(int(element))
	ch=input("Want to enter more elements? y/n: ")
even,odd=0,0
for num in l1:
	if num%2==0:
		even=even+1
	else:
		odd=odd+1
print("Odd numbers=%d\nEven numbers=%d" %(odd,even))
	
		
	 
	
                 
	 
                


