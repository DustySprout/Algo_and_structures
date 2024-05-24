# 3 лаба
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value})"

    def subtree(self):
        nodes = []
        self._subtree_helper(nodes)
        return nodes

    def _subtree_helper(self, nodes):
        if self.left is not None:
            self.left._subtree_helper(nodes)
        nodes.append(self)
        if self.right is not None:
            self.right._subtree_helper(nodes)


def find_successor(node: Node) -> Optional[Node]:
    if node.right is not None:
        return min(node.right.subtree(), key=lambda x: x.value)

    current = node
    while current.parent is not None and current.parent.right == current:
        current = current.parent

    if current.parent is None:
        return None
    return current.parent
