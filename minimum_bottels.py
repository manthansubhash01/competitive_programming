# codechef staters 170 contest
# Minimum Bottles
'''There are N identical water bottles, each of which has a capacity of X liters.
The i th bottle initially contains Ai liters of water.

You want to go on a trip and want to carry all your water with you.
However, to not make packing a hassle, you also want to carry the least number of bottles with you.

You can transfer any amount of water from one bottle to another, provided there is no spillage and no bottle contains more than 
X liters. Water from one bottle can be transferred to different bottles if you wish to do that.
What is the minimum number of bottles that you can carry with you, while still having all your water?

Input Format
The first line of input will contain a single integer T , denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains two space-separated integers N and X — the number of bottles and capacity of each bottle in liters, respectively.
The second line contains  N space separated integers 
A1,A2,…,AN denoting the volume of water in liters filled in each bottle.

Output Format
For each test case, output on a new line the minimum number of bottles that can be carried.

Constraints:    1≤T≤100
                1≤N≤100
                1≤X≤1000
                1≤Ai≤X
Sample 1:
Input :
2
3 10
1 2 3
4 2
1 2 2 1

Output :
1
3
Explanation:
Test case 
1
1: Transfer all the water from the second and third bottles into the first bottle.
The first bottle will now contain 6 liters of water (which is within its capacity of X=10), while the second and third bottles will be empty.
So, we only need to carry the first bottle with us.

More Info
Time limit1 secs
Memory limit1.5 GB
Source Limit50000 Bytes'''

import math
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    lst = list(map(int,input().split()))
    su = sum(lst)
    print(math.ceil(su/x))