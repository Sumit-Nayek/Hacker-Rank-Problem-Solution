'''
Given an array of integers, calculate the ratios of its elements that are , , and . Print the decimal value of each fraction on a new line with 6 places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
Example

There are  elements: two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
0.400000
0.400000
0.200000
Function Description
Complete the  function with the following parameter(s):
: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
Input Format
The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .
Constraints


Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output
0.500000
0.333333
0.166667
'''

def count_ratio(array):
    positive_c=0
    negative_c=0
    zero=0
    for num in array:
        if num>0:
            positive_c+=1
        elif num<0:
            negative_c+=1
        else:
            zero+=1
    return [positive_c/len(array),negative_c/len(array),zero/len(array)]
    
n=int(input())
array= list(map(int, input().split()))
result=count_ratio(array)
print(result[0])
print(result[1])
print(result[2])
