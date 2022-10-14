"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    result1 = sorted_arr[:4]
    result2 = sorted_arr[1:5]
    print(sum(result1), sum(result2))
