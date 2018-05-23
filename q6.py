#Q.6-Implement a stack and queue using lists.


choice=input("Enter 1 for stack or 2 for queue 3 to exit: ")
if choice=='1':
        print("Implementing stack")
        l1=[]
        ch='y'
        while ch=='y':
                c1=input("Enter 1 to push or 2 to pop: ")
                if c1=='1':
                        element=input("Enter element to be pushed: ")
                        l1.append(element)
			
                elif c1=='2':
                        if len(l1)==0:
                                print("Stack underflow")
                                break
                        l1.pop()
		
                else:
                        print("Wrong Choice")
                        break

                print("The Stack is as follows now:")
                print(l1)
		
                ch=input("Want to continue stack implementation? y/n: ")
elif choice=='2':
        print("Implementing Queue")
        l1=[]
        ch='y'
        while ch=='y':
                c1=input("Enter 1 to Enqueue or 2 to Dequeue: ")
                if c1=='1':
                        element=input("Enter element to be Added in Queue: ")
                        l1.append(element)
			
                elif c1=='2':
                        if len(l1)==0:
                                print("Queue underflow")
                                break
                        l1.pop(0)
		
                else:
                        print("Wrong Choice")
                        break

                print("The Queue is as follows now:")
                print(l1)
		
                ch=input("Want to continue Queue implementation? y/n :")
		
			
			
	
	

			

else:
        print("Exiting")

print("Program Ended")
