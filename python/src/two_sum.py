# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_1, num_1 in enumerate(
            nums
        ):  # for all options for number 1 + the index of it
            for i_2, num_2 in enumerate(
                nums
            ):  # for all options for number 2 + the index of it
                if i_1 == i_2:  # if have the same entry twice, skip
                    continue

                if target == num_1 + num_2:  # if we found our match, return it
                    return [i_1, i_2]

        return (
            []
        )  # if there was no match (not supposed to ever happen), return empty list, since return type says it must be a list
