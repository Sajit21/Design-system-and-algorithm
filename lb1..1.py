

#each steps should be run for n number from 10 t0 100
lab 1 def bubblesort(a,n):
  steps=0
  for i in range(1,n):#no of process
    for j in range (n-i):
      if(a[j+1]<a[j]):
          temp=a[j+1]
          a[j+1]=a[j]
          a[j]=temp
          steps=steps+6
        # The following line was unindented, causing the error.
      steps=steps+3 #This line should be inside the inner for loop to count steps correctly
    steps=steps+2
  bsteps.append(steps)
  print("No of steps(bubble):",steps)

def selectionsort(b,n):
    steps=0
    for i in range (1,n):#no of process
      min=b[i-1]
      mi=i-1
      steps=steps+4
      for j in range(i,n):#finds min
        if(b[j]<min):
          min=b[j]
          mi=j;
          steps=steps+5
        steps=steps+3
      temp=b[i-1]
      b[i-1]=b[mi]
      b[mi]=temp
      steps=steps+3
    ssteps.append(steps)
    print("No of steps(Selection):",steps)

#driven code

import random
bsteps=[]
ssteps=[]
for j in range(0,10):
  n=int(input("Enter n:"))
  a= []
  b= []
  for i in range(n):
    e=random.randint(0,n)
    a.append(e)
    b.append(e)
  bubblesort(a,n)
  print("Sorted data(bubble):",a)
  selectionsort(b,n)
  print("Sorted data(Selection):",b)
