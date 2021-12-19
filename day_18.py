import input_18
import unittest
import uuid
import math
from aoc import advent_of_code


class Node:
    def __init__(self, parent=None, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent
        self.unique = str(uuid.uuid4())

    def add(self, child):
        if self.left == None:
            self.left = child
        else:
            self.right = child

    def to_snail_number(self):
        if self.value != None:
            return self.value

        return [self.left.to_snail_number(), self.right.to_snail_number()]

    def to_the_right(self, child):
        res = []
        self.to_siblings(res)
        uniques = list(map(lambda x: x.unique, res))
        index = uniques.index(child.unique) + 1
        return res[index] if len(res) > index else None

    def to_the_left(self, child):
        res = []
        self.to_siblings(res)
        uniques = list(map(lambda x: x.unique, res))
        index = uniques.index(child.unique) - 1
        return res[index] if index >= 0 else None

    def to_siblings(self, res):
        if self.value != None:
            res.append(self)
            return

        self.left.to_siblings(res)
        self.right.to_siblings(res)

        return res

    def replace(self, replacement):
        if self.parent.left == self:
            self.parent.left = replacement
        else:
            self.parent.right = replacement

        replacement.parent = self.parent
        self.parent = None  # not needed, but cleaner

    @staticmethod
    def from_snail_number(input, root):
        for elem in input:
            if isinstance(elem, list):
                pair = Node(root)
                root.add(pair)
                Node.from_snail_number(elem, pair)
            else:
                root.add(Node(root, elem))

        return root


def add(l, r):
    root = Node()
    root.left = l
    root.right = r
    l.parent = root
    r.parent = root
    return root


def find_action(tree):
    explode = []
    split = []
    visit(tree, 0, explode, split)
    return {"explode": explode, "split": split}


def visit(tree, depth, explode, split):
    if depth >= 4 and tree.value == None:
        explode.append(tree)
        return

    if tree.value != None:
        if tree.value > 9:
            split.append(tree)
        return

    visit(tree.left, depth + 1, explode, split)
    visit(tree.right, depth + 1, explode, split)


def explode(root, node):
    to_the_left = root.to_the_left(node.left)
    to_the_right = root.to_the_right(node.right)

    if to_the_left:
        to_the_left.value += node.left.value

    if to_the_right:
        to_the_right.value += node.right.value

    node.replace(Node(None, 0))


def split(node):
    new_node = Node()
    new_node.add(Node(new_node, math.floor(node.value / 2)))
    new_node.add(Node(new_node, math.ceil(node.value / 2)))
    node.replace(new_node)


def apply_reductions(tree):
    actions = find_action(tree)
    if actions["explode"]:
        explode(tree, actions["explode"][0])
        apply_reductions(tree)
    elif actions["split"]:
        split(actions["split"][0])
        apply_reductions(tree)

    return tree


def add_all(input):
    root = Node.from_snail_number(input[0], Node())
    for next_line in input[1:]:
        next_tree = Node.from_snail_number(next_line, Node())
        root = add(root, next_tree)
        apply_reductions(root)

    return root.to_snail_number()


def magnitude(snail_number):
    lefty = snail_number[0]
    if isinstance(snail_number[0], list):
        lefty = magnitude(snail_number[0])
    else:
        lefty = snail_number[0]

    right = snail_number[1]
    if isinstance(snail_number[1], list):
        right = magnitude(snail_number[1])
    else:
        right = snail_number[1]

    return lefty * 3 + right * 2


def part_one(input):
    root = add_all(input)
    return magnitude(root)


def part_two(input):
    max_so_far = 0

    for idx_a, elem in enumerate(input):
        for idx_b, elem in enumerate(input):
            a = input[idx_a]
            b = input[idx_b]

            if idx_a == idx_b:
                continue

            mag = part_one([a, b])
            if mag > max_so_far:
                max_so_far = mag

            mag = part_one([b, a])
            if mag > max_so_far:
                max_so_far = mag

    return max_so_far


advent_of_code(
    {
        "day": 18,
        "part": 1,
        "fn": part_one,
        "sample": input_18.sample(),
        "expected": 4140,
        "real": input_18.real(),
    }
)

advent_of_code(
    {
        "day": 18,
        "part": 2,
        "fn": part_two,
        "sample": input_18.sample(),
        "expected": 3993,
        "real": input_18.real(),
    }
)


class TestTree(unittest.TestCase):
    def test_create(self):
        root = Node.from_snail_number([3, [1, 2]], Node())
        self.assertEqual([3, [1, 2]], root.to_snail_number())

    def test_get_right(self):
        root = Node.from_snail_number([3, [1, 2]], Node())
        self.assertEqual(1, root.to_the_right(root.left).value)
        self.assertEqual(2, root.to_the_right(root.right.left).value)
        self.assertEqual(None, root.to_the_right(root.right.right))

    def test_get_left(self):
        root = Node.from_snail_number([3, [1, 2]], Node())
        self.assertEqual(1, root.to_the_left(root.right.right).value)
        self.assertEqual(3, root.to_the_left(root.right.left).value)
        self.assertEqual(None, root.to_the_left(root.left))

    def test_replace_pair_with_value(self):
        root = Node.from_snail_number([3, [1, 2]], Node())
        root.right.replace(Node(None, 0))
        self.assertEqual([3, 0], root.to_snail_number())

    def test_replace_value_with_pair(self):
        root = Node.from_snail_number([3, [1, 2]], Node())
        new_node = Node()
        new_node.add(Node(None, 8))
        new_node.add(Node(None, 9))
        root.left.replace(new_node)
        self.assertEqual([[8, 9], [1, 2]], root.to_snail_number())


class TestProblem(unittest.TestCase):
    def test_add(self):
        left = Node.from_snail_number([1, 2], Node())
        right = Node.from_snail_number([[3, 4], 5], Node())
        expected = [[1, 2], [[3, 4], 5]]
        self.assertEqual(add(left, right).to_snail_number(), expected)

    def test_check_for_explode(self):
        root = Node.from_snail_number([[[[[9, 8], 1], 2], 3], 4], Node())
        node_to_explode = root.left.left.left.left
        self.assertEqual(find_action(root)["explode"][0], node_to_explode)

    def test_explode_examples(self):
        self.exploder([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4])
        self.exploder([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]])
        self.exploder([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3])
        self.exploder(
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        )
        self.exploder(
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        )

    def exploder(self, input, expected):
        root = Node.from_snail_number(input, Node())
        node_to_explode = find_action(root)["explode"][0]
        explode(root, node_to_explode)
        self.assertEqual(root.to_snail_number(), expected)

    def test_check_for_split(self):
        root = Node.from_snail_number([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], Node())
        node_to_split = root.left.right.left
        self.assertEqual(find_action(root)["split"][0], node_to_split)

    def test_split_examples(self):
        self.splitter(
            [[[[0, 7], 4], [15, [0, 13]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
        )
        self.splitter(
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]],
        )

    def splitter(self, input, expected):
        root = Node.from_snail_number(input, Node())
        node_to_explode = find_action(root)["split"][0]
        split(node_to_explode)
        self.assertEqual(root.to_snail_number(), expected)

    def test_apply_reductions(self):
        tree = Node.from_snail_number([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], Node())
        expected = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

        result = apply_reductions(tree)
        self.assertEqual(result.to_snail_number(), expected)

    def test_add_and_reduce_example(self):
        input = [
            [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
            [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
            [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
            [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
            [7, [5, [[3, 8], [1, 4]]]],
            [[2, [2, 2]], [8, [8, 1]]],
            [2, 9],
            [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
            [[[5, [7, 4]], 7], 1],
            [[[[4, 2], 2], 6], [8, 7]],
        ]
        expected = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]

        self.assertEqual(expected, add_all(input))

    def test_magnitude(self):
        self.magni([9, 1], 29)
        self.magni([1, 9], 21)
        self.magni([[9, 1], [1, 9]], 129)
        self.magni([[1, 2], [[3, 4], 5]], 143)
        self.magni([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384)
        self.magni([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445)
        self.magni(
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488
        )

    def magni(self, input, expected):
        self.assertEqual(magnitude(input), expected)


unittest.main()
