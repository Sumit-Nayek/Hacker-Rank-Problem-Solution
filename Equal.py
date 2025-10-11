'''
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.
To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give  pieces to all but one colleague. Everyone who gets a piece in a round receives the same number of pieces.
Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the same number of pieces.
Example
arr=[1,1,5]
Arr represents the starting numbers of 2 pieces for each colleague. She can give  pieces to the first two and the distribution is then . On the next round, she gives the same two  pieces each, and everyone has the same number:  . Return the number of rounds, .
Function Description
Complete the equal function in the editor below.
equal has the following parameter(s):
int arr[n]: the integers to equalize
Returns
int: the minimum number of operations required
Input Format
The first line contains an integer t, the number of test cases.
Each test case has  lines 2.
- The first line contains an integer , the number of colleagues and the size of arr.
- The second line contains n space-separated integers arr[i] , the numbers of pieces of chocolate each colleague has at the start.
Constraints
1<=t<=100
1<=n<=1000
The number of chocolates each colleague has initially < 1000.
'''

def min_operations_to_equal(arr):
    # Allowed decrements per operation are 5, 2, 1.
    min_val = min(arr)
    best = None

    # Try targets min_val, min_val-1, ..., min_val-4
    for base in range(min_val, min_val - 5, -1):
        total_ops = 0
        for x in arr:
            diff = x - base
            # Number of 5s
            c5 = diff // 5
            diff %= 5
            # Number of 2s
            c2 = diff // 2
            diff %= 2
            # Number of 1s
            c1 = diff
            total_ops += (c5 + c2 + c1)

        if best is None or total_ops < best:
            best = total_ops

    return best


# ---------- Input reading ----------
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(min_operations_to_equal(arr))
