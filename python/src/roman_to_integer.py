# https://leetcode.com/problems/roman-to-integer/
class Solution:
    numeral_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numeral_order = [x for x in numeral_values]

    def romanToInt(self, s: str) -> int:
        value = 0
        for i in range(len(s)):
            current_numeral = s[i]

            if i < len(s) - 1:
                next_numeral = s[i + 1]
            else:
                next_numeral = None

            if next_numeral != None and (self.numeral_order.index(current_numeral) < self.numeral_order.index(next_numeral)):
                value -= self.numeral_values[current_numeral]
            else:
                value += self.numeral_values[current_numeral]

        return value