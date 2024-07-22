msteps = 0
qsteps = 0

def mergesort(a, l, r):
    global msteps
    if l < r:  # If the dataset has more than 1 element
        m = (l + r) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)
        msteps += 1  # Counting the merge function call

def merge(a, l, m, r):
    global msteps
    i = l
    j = m + 1
    k = l
    b = [0] * len(a)  # Temporary array for merging

    while i <= m and j <= r:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
        msteps += 6  # Counting steps in the merge operation

    while i <= m:
        b[k] = a[i]
        i += 1
        k += 1
        msteps += 4  # Counting steps in the merge operation

    while j <= r:
        b[k] = a[j]
        j += 1
        k += 1
        msteps += 4  # Counting steps in the merge operation

    for i in range(l, r + 1):
        a[i] = b[i]
        msteps += 3  # Counting steps in copying back to the original array

def quicksort(c, l, r):
    global qsteps
    if l < r:
        p = partition(c, l, r)
        quicksort(c, l, p - 1)
        quicksort(c, p + 1, r)
        qsteps += 1  # Counting the partition function call

def partition(c, l, r):
    global qsteps
    pivot = c[l]
    x = l + 1
    y = r

    while x <= y:
        while x <= y and c[x] <= pivot:
            x += 1
            qsteps += 4
        while x <= y and c[y] > pivot:
            y -= 1
            qsteps += 3
        if x < y:
            swap(c, x, y)
            qsteps += 2

    swap(c, l, y)
    qsteps += 1
    return y

def swap(c, i, j):
    global qsteps
    c[i], c[j] = c[j], c[i]
    qsteps += 3

# Driver code
import random
n = int(input("Enter n: "))
a = []
c = []

for i in range(n):
    e = random.randint(0, n)
    a.append(e)
    c.append(e)

b = [None] * n
mergesort(a, 0, n - 1)
print("Sorted data (Merge Sort):", a)
print("#steps (Merge Sort) =", msteps)

quicksort(c, 0, n - 1)
print("Sorted data (Quick Sort):", c)
print("#steps (Quick Sort) =", qsteps)
