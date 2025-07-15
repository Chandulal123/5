#assignment 5 Task 1: Create a Dictionary of Student Marks

dictionary={'ravi': 25, 'chandu': 82,'girish': 78,'nagu': 60}
n=input('enter the students name : ' )

if n in dictionary:
    print(n,'s mark : ',dictionary[n])
else:
    print('student',n,'not found')

#assignment 5 task 2 :Demonstrate List Slicing

n=[1,2,3,4,5,6,7,8,9,10]
m=n[0:5]
l=m[::-1]
print('original list : ',n)
print('extracted first five element : ',m)
print('extracted first five element : ',l)



