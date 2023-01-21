# https://leetcode.com/problems/fancy-sequence/
class Fancy:
    def __init__(self):
        self.data = []  # make list as underlying datastructure

        self.operations = []  # make a list to save the todo operation in

    def append(self, val: int) -> None:
        self.data.append(val)  # append to data

    def addAll(self, inc: int) -> None:
        self.operations.append(
            ("+", inc, len(self.data) - 1)
        )  # add "+ inc" to the list of operations todo, apply only on current data

    def multAll(self, m: int) -> None:
        self.operations.append(
            ("*", m, len(self.data) - 1)
        )  # add "* m" to the list of operations todo, apply only on current data

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.data):  # if out of bounds, return -1
            return -1

        value = self.data[idx]  # get value, and perform all operations on it
        for operation, amount, until_index in self.operations:
            if idx > until_index:  # if operation came before data, ignore step
                continue

            if operation == "+":
                value += amount
            else:
                value *= amount

        return value % 1000000007  # return value with modulo 10⁹ + 7
