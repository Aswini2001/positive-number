print ('\t\t\tchecking postive numbers')
 
mylist = []
print("enter 5 integers to check")
i =0
while i<5:
    r=int(input())
    mylist.append(r)
    
    i=i+1
print("input: ")
print(mylist)
print("output: ")
n =0
while n<5:
    if (mylist[n]>0):
       print(mylist[n], end=" ")
       
    n=n+1
