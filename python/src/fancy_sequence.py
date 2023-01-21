# https://leetcode.com/problems/fancy-sequence/
class Fancy:
    def __init__(self):
        self.data = []  # make list as underlying datastructure

    def append(self, val: int) -> None:
        self.data.append(val)  # append to data

    def addAll(self, inc: int) -> None:
        for i in range(len(self.data)):  # increase each value
            self.data[i] += inc

    def multAll(self, m: int) -> None:
        for i in range(len(self.data)):  # multiply each value
            self.data[i] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.data):  # if out of bounds, return -1
            return -1

        return self.data[idx] % 1000000007  # else return value with modulo 10⁹ + 7
