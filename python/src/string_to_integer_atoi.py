# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        I realize i could have just used int() on the whole string after sanatizing, but that would ignore the point of this taks completly.
        """

        s = s.strip()  # remove whitespace at the start and end

        pre_digit_s = ""  # check all indicators
        for c in s:
            if c.isdigit():
                break

            pre_digit_s += c

        if pre_digit_s.count("-") + pre_digit_s.count("+") > 1:  # return 0 if invalid
            return 0

        negative = s.startswith("-")  # check if negative
        s = s.strip("-+")  # remove indicators

        result = 0
        for c in s:
            if not c.isdigit():  # if no more digits, break for loop
                break

            result *= 10  # make the digit(s) before have their actual value (42 -> 4 = 4, next digit 4*10 = 40, 2 = 2, result = 42)
            result += int(c)

        if negative:  # negate if it was a negativ number
            result *= -1

        # restrict result to 32bit integer value
        if result < -2147483648:
            result = -2147483648
        elif result > 2147483647:
            result = 2147483647

        return result
