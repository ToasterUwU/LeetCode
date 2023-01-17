# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = nums1 + nums2
        combined_list.sort()

        combined_list_len = len(combined_list)
        if combined_list_len % 2 == 0:
            middle_a = int((combined_list_len - 1) / 2)
            middble_b = middle_a + 1
            return (combined_list[middle_a] + combined_list[middble_b]) / 2
        else:
            return combined_list[int(combined_list_len / 2)]
