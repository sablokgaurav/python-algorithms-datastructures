#https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
#Find Three Consecutive Integers That Sum to a Given Number
#Given an integer num, return three consecutive integers (as a sorted array) that sum to num. 
#If num cannot be expressed as the sum of three consecutive integers, return an empty array.
#Example 1:
#Input: num = 33
#Output: [10,11,12]
#Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
#10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
#Example 2:
#Input: num = 4
#Output: []
#Explanation: There is no way to express 4 as the sum of 3 consecutive integers.

list(filter(lambda n: sum(n)==33,(filter(lambda n: n[0]+1==n[1] and n[1]+1==n[2],
                   [(a,b,c) for a in range(34) for b in range(34) for c in range(num)]))))