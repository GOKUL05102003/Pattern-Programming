n=int(input("Enter the no. of Rows: "))
for i in range(1,n+1):
    print("*"if(i==1)else("*"+" "*(i-2)+"*")if(i!=n)else "*"*n)

'''
n=int(input("Enter the no. of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

OR

n=int(input("Enter the no. of Rows: "))
if n>=1:
    print("*")
for i in range(2,n):
    print("*"+" "*(i-2)+"*")
if n>1:
    print("*"*n)
'''
'''
Enter the no. of Rows: 5
*
**
* *
*  *
*****
'''