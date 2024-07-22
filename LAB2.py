def insertionsort(a, n):
    steps = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        steps += 4
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            steps += 4
        a[j + 1] = key
        steps += 1
    print("no of steps(insertion)", steps)
    

def selectionsort(b, n):
    steps = 0
    for i in range(1,n):
        min=b[i-1]
        mi = i-1
        for j in range(i, n):
            if b[j] < b[mi]:
                min=b[j]
                mi = j
                steps += 5
            steps=steps+3
        temp=b[i-1]
        b[i-1] = b[mi]
        b[mi]=temp
        steps += 3
    print("no of steps(selection)", steps)


# Driver code
import random

n = int(input("Enter n: "))
a = []
b = []

for i in range(n):
    e = random.randint(0, n)
    a.append(e)
    b.append(e)

print("Original data:", a)
insertionsort(a, n)
print("Sorted data (insertion):", a)
#print("Total steps (insertion):", steps_insertion)

selectionsort(b, n)
print("Sorted data (selection):", b)
#print("Total steps (selection):", steps_selection)
