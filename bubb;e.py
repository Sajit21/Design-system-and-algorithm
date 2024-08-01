//random code using chatgpt which give a graphical form 


import random
import matplotlib.pyplot as plt

def bubblesort(a):
    steps = 0
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            steps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps += 3
    return steps

def selectionsort(b):
    steps = 0
    n = len(b)
    for i in range(n):
        minindex = i
        for j in range(i + 1, n):
            steps += 1
            if b[j] < b[minindex]:
                minindex = j
                steps += 1
        if minindex != i:
            b[i], b[minindex] = b[minindex], b[i]
            steps += 3
    return steps

bubble_steps = []
selection_steps = []

n = int(input("Enter the value of n: "))

for j in range(10):
    a = [random.randint(0, n) for _ in range(n)]
    b = a[:]

    bsteps = bubblesort(a)
    bubble_steps.append(bsteps)
    print(f"Bubble sort Sorted: {a}")

    ssteps = selectionsort(b)
    selection_steps.append(ssteps)
    print(f"Selection sort Sorted: {b}")

print("Bubble sort steps:", bubble_steps)
print("Selection sort steps:", selection_steps)

plt.figure(figsize=(10, 5))
plt.plot(range(10), bubble_steps, marker='o', label='Bubble Sort Steps')
plt.plot(range(10), selection_steps, marker='o', label='Selection Sort Steps')
plt.xlabel('Trial')
plt.ylabel('Number of Steps')
plt.title('Bubble Sort vs. Selection Sort Steps')
plt.legend()
plt.grid(True)
plt.show()
