# //some changews have to be done so the chart can be done in increasing order

def bubblesort(a,n):
 steps=0
 for i in range(1,n):
    for j in range(n-1):
       if(b[j+1]<b[j]):
          temp=b[j+1]
          b[j+1]=b[j]
          b[j]=temp
          steps=steps+6
          steps=steps+3
          steps=steps+2
          print("no of steps(bubble)",steps)
def selectionsort(b,n):
 steps=0
 for i in range(1,n):
    min=b[i-1]
    mi=i-1
    steps=steps+4
    for j in range(i,n):
          if(b[j]<min):
             min=b[j]
             mi=j
             steps=steps+5
             steps=steps+3
             temp=b[i-1]
             b[i-1]=b[mi]
             b[mi]=temp
             steps=steps+3
          print("no of steps(selection)",steps)


 

         




#driver code
import random
n= int(input("enter n number:"))
a=[]
b=[]
for i in range(n):
    e=random.randint(0,n)
    a.append(e)
    b.append(e)

bubblesort(a,n)
print("sorted data bubble",a)
selectionsort(b,n)
print("sorted data selection ", b)       
