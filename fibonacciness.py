# There is an array of 5
#  integers. Initially, you only know 𝑎1,𝑎2,𝑎4,𝑎5 .
# You may set 𝑎3 to any positive integer, negative integer, or zero. The Fibonacciness of the array is the number of integers 𝑖
#  (1≤𝑖≤3) such that 𝑎𝑖+2=𝑎𝑖+𝑎𝑖+1 .
#  Find the maximum Fibonacciness over all integer values of 𝑎3.

# Input
# The first line contains an integer 𝑡
#  (1≤𝑡≤500
# ) — the number of test cases.

# The only line of each test case contains four integers 𝑎1,𝑎2,𝑎4,𝑎5
#  (1≤𝑎𝑖≤100).

# Output
# For each test case, output the maximum Fibonacciness on a new line.

# sample input
# 6
# 1 1 3 5
# 1 3 2 1
# 8 10 28 100
# 100 1 100 1
# 1 100 1 100
# 100 100 100 100

# output 
# 3
# 2
# 2
# 1
# 1
# 2

# Note
# In the first test case, we can set 𝑎3 to 2 to achieve the maximal Fibonacciness of 3.

# In the third test case, it can be shown that 2 is the maximum Fibonacciness that can be achieved. This can be done by setting 𝑎3
#  to 18 .
# time limit per test1 second
# memory limit per test256 megabytes

t = int(input())
for i in range(t) :
    lst = list(map(int,input().split()))
    l , r = 0 , 1 
    d = {}
    while r < 4 and l < 3 :
        if l == 0 and r == 1 :
            x = lst[l] + lst[r]
            d[x] = 1 
            l +=1 
            r += 1
        elif l == 1 and r == 2 :
            x = lst[r] - lst[l]
            if x in d :
                d[x] += 1 
            else:
                d[x] = 1
            l +=1 
            r += 1
        elif l == 2 and r == 3 :
            x = lst[r] - lst[l]
            if x in d :
                d[x] += 1 
            else:
                d[x] = 1
            l +=1 
            r += 1
    print(max(d.values()))
