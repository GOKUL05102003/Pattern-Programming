n=int(input("Enter the no. of Rows: "))
for i in range(1,n+1):
    print(" "*(n-i)+("*" if(i==1)else("*"+" "*(i-2)+"*")if(i!=n)else "*"*n))
'''
n=int(input("Enter the no. of Rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        if k==1 or k==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
Enter the no. of Rows: 5
    *
   **
  * *
 *  *
*****
'''