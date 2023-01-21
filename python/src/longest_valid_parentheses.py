# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_streak = 0  # return value for later

        i = 0  # index of what we are looking at
        while True:  # while index is not out of range
            streak = 0
            
            

        return longest_streak

    # def longestValidParentheses(self, s: str) -> int:
    #     longest_streak = 0  # return value for later
    #     i = 0  # index of what we are looking at
    #     while i < len(s):  # while index is not out of range
    #         streak = 0
    #         if s[i] == "(":  # start streak
    #             while i < len(s):  # while index within bounds
    #                 streak += 1  # ( is worth 1
    #                 if (
    #                     streak % 2 == 0
    #                 ):  # evvery second part of streak should be a ) -> 1( 2) 1( 2) 1( 2)
    #                     if s[i] != ")":
    #                         break
    #                 else:
    #                     if s[i] != "(":  # every first part should be a (
    #                         break

    #                 i += 1  # look at next char

    #             if (
    #                 streak % 2 == 1
    #             ):  # if streak ended on a (, its not allowed to get a point for that (, so remove it
    #                 streak -= 1

    #             if streak > longest_streak:  # set new longest streak if needed
    #                 longest_streak = streak
    #         else:
    #             i += 1  # if streak didnt start, look at next char

    # return longest_streak
