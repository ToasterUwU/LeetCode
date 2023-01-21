# https://leetcode.com/problems/first-missing-positive/
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1  # assume 1 is missing now
        for num in sorted(nums):  # go over all numbers in a sorted iterator
            if num <= 0:  # ignore negative values and 0
                continue

            if (
                num == missing
            ):  # if num is the "probably missing" number, assume next might be missing
                missing = num + 1
            elif (
                num > missing
            ):  # else if num is bigger than missing, break the loop and return missing
                break

        return missing
