'''
Given an amount and the denominations of coins available, determine how many ways change can be made for amount. There is a limitless supply of each coin type.
Example


There are  ways to make change for : , , and .
Function Description
Complete the getWays function in the editor below.
getWays has the following parameter(s):
int n: the amount to make change for
int c[m]: the available coin denominations
Returns
int: the number of ways to make change
Input Format
The first line contains two space-separated integers  and , where:
 is the amount to change
 is the number of coin types
The second line contains  space-separated integers that describe the values of each coin type.
Constraints



Each  is guaranteed to be distinct.
'''

def getWays(n, coins):
    # ways[x] = number of ways to make amount x
    ways = [0] * (n + 1)
    ways[0] = 1

    # for each coin, update ways for all amounts >= coin
    for coin in coins:
        for amount in range(coin, n + 1):
            ways[amount] += ways[amount - coin]

    return ways[n]


# ---------- Input reading (HackerRank style) ----------
n, m = map(int, input().split())     # n = amount, m = number of coin types
coins = list(map(int, input().split()))

# ---------- Output ----------
print(getWays(n, coins))
