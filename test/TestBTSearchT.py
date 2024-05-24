import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(node: BinaryTree) -> BinaryTree:
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent


class TestFindSuccessor(unittest.TestCase):
    def test_find_successor(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5, BinaryTree(3), BinaryTree(7))
        root.right = BinaryTree(15, right=BinaryTree(20, BinaryTree(12)))
        root.left.parent = root
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.parent = root
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right

        # Test cases
        self.assertEqual(find_successor(root.left.right), root)
        self.assertEqual(find_successor(root.left), root.left.right)
        self.assertEqual(find_successor(root.left.left), root.left)
        self.assertEqual(find_successor(root.right), root.right.right.left)
        self.assertEqual(find_successor(root.right.right), None)


if __name__ == '__main__':
    unittest.main()
