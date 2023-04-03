#! /usr/bin/env python3

# --------------------------------------------------------------------
import os
import unittest

# --------------------------------------------------------------------
if "SOLUTIONS" in os.environ:
    midterm1 = __import__(os.environ["SOLUTIONS"])
else:
    import midterm1

# --------------------------------------------------------------------
class TwoSum(unittest.TestCase):
    VECTORS = [
        dict(input=([2, 7, 11, 15], 9), output=(0, 1)),
        dict(input=([3, 2, 4], 6), output=(1, 2)),
        dict(input=([3, 3], 6), output=(0, 1)),
    ]

    def test_two_sum(self):
        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                self.assertEqual(midterm1.two_sum(*v["input"]), v["output"])


# --------------------------------------------------------------------
class Climb(unittest.TestCase):
    VECTORS = [
        dict(input=(2,), output=2),
        dict(input=(3,), output=3),
        dict(input=(10,), output=89),
    ]

    def test_climb(self):
        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                self.assertEqual(midterm1.climb(*v["input"]), v["output"])


# --------------------------------------------------------------------
class Happy(unittest.TestCase):
    VECTORS = [
        dict(input=(19,), output=True),
        dict(input=(2,), output=False),
    ]

    def test_happy(self):
        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                self.assertEqual(midterm1.happy(*v["input"]), v["output"])


# --------------------------------------------------------------------
class PerfectSquareSum(unittest.TestCase):
    VECTORS = [
        dict(input=(12,), output=3),
        dict(input=(13,), output=2),
    ]

    def test_happy(self):
        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                self.assertEqual(midterm1.perfect_square_sum(*v["input"]), v["output"])


# --------------------------------------------------------------------
class CheckBoard(unittest.TestCase):
    def test_checkboard(self):
        P = [
            [10, 13, 47, 96, 8],
            [11, 5, 24, 3, 41],
            [34, 5, 12, 23, 9],
            [1, 22, 12, 14, 28],
        ]
        m, n = len(P), len(P[0])
        aout = 21

        with self.subTest(f"{(m, n, P)} --> {aout}"):
            self.assertEqual(midterm1.checkboard(len(P), len(P[0]), P), aout)


# --------------------------------------------------------------------
class AllPaths(unittest.TestCase):
    VECTORS = [
        dict(
            input=(
                5,
                [[4, 3, 1], [3, 2, 4], [3], [4], []],
            ),
            output=[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        )
    ]

    def test_allpaths(self):
        def canon(l):
            return (len(l), set(tuple(x) for x in l))

        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                mine = v["output"]
                their = midterm1.all_paths(*v["input"])
                self.assertEqual(canon(their), canon(mine))


# --------------------------------------------------------------------
class LoudAndRich(unittest.TestCase):
    VECTORS = [
        dict(
            input=(
                [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                [3, 2, 5, 4, 6, 1, 7, 0],
            ),
            output=[5, 5, 2, 5, 4, 5, 6, 7],
        ),
        dict(input=([], [0]), output=[0]),
    ]

    def test_loud_and_rich(self):
        for v in self.VECTORS:
            with self.subTest(f'{v["input"]} --> {v["output"]}'):
                self.assertEqual(midterm1.loud_and_rich(*v["input"]), v["output"])


# --------------------------------------------------------------------
class Diet(unittest.TestCase):
    def repr_node(self, node):
        if node is None:
            return "."
        aout = [
            ("lo", repr(node.lo)),
            ("hi", repr(node.hi)),
            ("left", self.repr_node(node.left)),
            ("right", self.repr_node(node.right)),
        ]
        aout = [f"{k}={v}" for k, v in aout]
        aout = ", ".join(aout)
        return f"DietNode[{aout}]"

    def create(self):
        node = midterm1.DietNode(
            lo=5,
            hi=10,
            left=midterm1.DietNode(lo=2, hi=2),
            right=midterm1.DietNode(lo=13, hi=14),
        )
        values = [2, 5, 6, 7, 8, 9, 10, 13, 14]
        return (node, values)

    def test_inorder(self):
        node, aout = self.create()

        with self.subTest(f"{self.repr_node(node)} --> {aout}"):
            self.assertEqual(node.inorder(), aout)

    def test_contains(self):
        node, values = self.create()
        tests = [2, 4, 6, 10, 13, 15, 17]

        for test in tests:
            aout = test in values
            with self.subTest(f"{(self.repr_node(node), test)} --> {aout}"):
                self.assertEqual(node.contains(test), aout)

    def test_invariant(self):
        node, _ = self.create()

        with self.subTest(f"{(self.repr_node(node),)} --> True"):
            self.assertEqual(node.check_diet_invariant(), True)

    def test_insert(self):
        node, values = self.create()
        newv = 12

        with self.subTest(f"{(self.repr_node(node), newv)}"):
            node.insert(newv)
            self.assertEqual(node.contains(12), True)
            self.assertEqual(node.check_diet_invariant(), True)


# --------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
