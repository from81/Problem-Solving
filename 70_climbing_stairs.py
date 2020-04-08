"""
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        approach
        1. use memoization to store intermediate computations of the # of steps one can take to get to the i-th step
        2. start backward from n-th step
        3. only 2 way to arrive at n-th step: 1 step from n-1-th step or 2 steps from n-2-th step
        """

        memo = {}

        def climb(n, memo):
            paths = 0

            if str(n) in memo.keys():
                paths = memo[str(n)]
            else:
                if n == 1:
                    paths = 1
                elif n == 2:
                    paths = 2
                elif n > 2:
                    paths = climb(n-1, memo) + climb(n-2, memo)

                memo[str(n)] = paths

            return paths

        return climb(n, memo)
