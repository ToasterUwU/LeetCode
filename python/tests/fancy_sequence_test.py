# https://leetcode.com/problems/fancy-sequence/

import unittest

from src.fancy_sequence import Fancy

test_cases = [
    {
        "kwargs": {
            "operations": [
                "append",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "getIndex",
                "getIndex",
            ],
            "inputs": [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]],
        },
        "correct_output": [
            None,
            None,
            None,
            None,
            10,
            None,
            None,
            None,
            26,
            34,
            20,
        ],
    },
    {
        "kwargs": {
            "operations": [
                "append",
                "getIndex",
                "multAll",
                "multAll",
                "getIndex",
                "addAll",
                "append",
                "append",
                "getIndex",
                "append",
                "append",
                "addAll",
                "getIndex",
                "multAll",
                "addAll",
                "append",
                "addAll",
                "getIndex",
                "getIndex",
                "multAll",
                "multAll",
                "multAll",
                "append",
                "addAll",
                "getIndex",
                "getIndex",
                "getIndex",
                "append",
                "getIndex",
                "addAll",
                "multAll",
                "append",
                "multAll",
                "addAll",
                "getIndex",
                "append",
                "append",
                "addAll",
                "getIndex",
                "multAll",
                "getIndex",
                "addAll",
                "getIndex",
                "multAll",
                "addAll",
                "getIndex",
                "addAll",
                "append",
                "append",
                "append",
                "multAll",
                "multAll",
                "append",
                "multAll",
                "addAll",
                "getIndex",
                "addAll",
                "multAll",
                "multAll",
                "multAll",
                "append",
                "multAll",
                "append",
                "multAll",
                "addAll",
                "append",
                "append",
                "getIndex",
                "getIndex",
                "getIndex",
                "addAll",
                "multAll",
                "multAll",
                "append",
                "append",
                "getIndex",
                "append",
                "append",
                "append",
                "getIndex",
                "getIndex",
            ],
            "inputs": [
                [5],
                [0],
                [14],
                [10],
                [0],
                [12],
                [10],
                [4],
                [2],
                [4],
                [2],
                [1],
                [1],
                [8],
                [11],
                [15],
                [12],
                [0],
                [3],
                [4],
                [11],
                [11],
                [10],
                [8],
                [2],
                [3],
                [0],
                [7],
                [3],
                [2],
                [6],
                [10],
                [6],
                [8],
                [7],
                [9],
                [9],
                [12],
                [0],
                [13],
                [7],
                [3],
                [4],
                [8],
                [14],
                [2],
                [9],
                [9],
                [9],
                [7],
                [5],
                [12],
                [9],
                [3],
                [8],
                [10],
                [14],
                [14],
                [14],
                [6],
                [1],
                [3],
                [11],
                [12],
                [6],
                [7],
                [13],
                [12],
                [5],
                [6],
                [1],
                [11],
                [11],
                [4],
                [9],
                [7],
                [11],
                [1],
                [3],
                [1],
                [0],
            ],
        },
        "correct_output": [
            None,
            5,
            None,
            None,
            700,
            None,
            None,
            None,
            4,
            None,
            None,
            None,
            11,
            None,
            None,
            None,
            None,
            5727,
            63,
            None,
            None,
            None,
            None,
            None,
            30500,
            30500,
            2771876,
            None,
            30500,
            None,
            None,
            None,
            None,
            None,
            332,
            None,
            None,
            None,
            99787628,
            None,
            4472,
            None,
            10651007,
            None,
            None,
            114201606,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            401588,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            69515718,
            633655703,
            831230656,
            None,
            None,
            None,
            None,
            None,
            715527902,
            None,
            None,
            None,
            728131107,
            601045500,
        ],
    },
]


class FancySequence(unittest.TestCase):
    def test_leet_code_examples(self):
        for test_case in test_cases:
            solution_obj = Fancy()
            funcs = {
                method: getattr(solution_obj, method)
                for method in dir(solution_obj)
                if callable(getattr(solution_obj, method))
                and not method.startswith("_")
            }

            for action, values, correct_output in zip(
                test_case["kwargs"]["operations"],
                test_case["kwargs"]["inputs"],
                test_case["correct_output"],
            ):
                self.assertEqual(funcs[action](*values), correct_output)


if __name__ == "__main__":
    unittest.main()
