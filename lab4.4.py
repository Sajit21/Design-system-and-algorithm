#main lab chai yo. yeta samah increasing order ma line graph banauna parcha

import random

# Initialize global variables
msteps = 0
hsteps = 0

def mergesort(a, l, r):
    global msteps
    if l < r:
        m = (l + r) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)
        msteps += 5
    msteps += 1

def merge(a, l, m, r):
    global msteps
    i = k = l
    j = m + 1
    b = [None] * len(a)
    msteps += 2
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
            k += 1
            msteps += 6
        else:
            b[k] = a[j]
            k += 1
            j += 1
            msteps += 5
    while i <= m:
        b[k] = a[i]
        k += 1
        i += 1
        msteps += 4
    while j <= r:
        b[k] = a[j]
        k += 1
        j += 1
        msteps += 4
    for i in range(l, r + 1):
        a[i] = b[i]
        msteps += 3
    msteps += 2

def heapsort(c, n):
    global hsteps
    buildheap(c, n)
    i = n
    hsteps += 2
    while i >= 1:
        swap(c, 1, n)
        n -= 1
        heapify(c, n, 1)
        i -= 1
        hsteps += 5
    hsteps += 1

def buildheap(c, n):
    global hsteps
    i = n // 2
    hsteps += 1
    while i >= 1:
        heapify(c, n, i)
        i -= 1
        hsteps += 3
    hsteps += 1

def heapify(c, n, i):
    global hsteps
    l = 2 * i
    r = 2 * i + 1
    largest = i
    hsteps += 3
    if l <= n and c[l] > c[largest]:
        largest = l
        hsteps += 3
    hsteps += 2
    if r <= n and c[r] > c[largest]:
        largest = r
        hsteps += 3
    hsteps += 2
    if largest != i:
        swap(c, i, largest)
        heapify(c, n, largest)
        hsteps += 3
    hsteps += 1

def swap(a, i, j):
    global hsteps
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    hsteps += 3

# Driver Code to run 10 different times sequentially
n = int(input("Enter n: "))

for trial in range(10):
    msteps = 0
    hsteps = 0
    a = []
    c = [None] * (n + 1)
    for i in range(n):
        e = random.randint(0, n)
        a.append(e)
        c[i + 1] = e
    b = [None] * n

    mergesort(a, 0, n - 1)
    print(f"Trial {trial + 1}:")
    print("Sorted data (mergesort):", a)
    print("#Steps (mergesort) =", msteps)

    heapsort(c, n)
    print("Sorted data (heapsort):", c[1:n + 1])
    print("#Steps (heapsort) =", hsteps)
    print()
