'''
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.
Example

The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.
Function Description
Complete the function  with the following parameter(s):
: the candle heights
Returns
: the number of candles that are tallest
Input Format
The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of candil[i].
'''

def birthday_cake_candle(array):
    count=0
    m=max(arr)
    for i in array:
        if m==i:
            count+=1
    return print(count)

n=int(input())
arr=list(map(int, input().split()))
birthday_cake_candle(arr)
