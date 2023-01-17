# https://leetcode.com/problems/relative-sort-array/
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def custom_sort(val: int):
            return arr2.index(val)

        not_in_arr2 = [x for x in arr1 if x not in arr2]
        arr1 = [x for x in arr1 if x not in not_in_arr2]

        arr1.sort(key=custom_sort) # sort by index in arr2
        arr1.extend(sorted(not_in_arr2)) # attach other values in ascending order to the end

        return arr1
