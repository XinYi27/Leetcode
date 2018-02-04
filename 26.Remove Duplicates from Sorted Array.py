#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[new]:
                new += 1
                nums[new]=nums[i]

        return new+1
