#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,n in enumerate(self.nums):
            m = self.target - n
            if m in d:
                return [d[m],i]
            else:
                d[n] = i

test = Solution([1, 2, 3, 4, 5, 6, 7],9)
print(test.twoSum())
