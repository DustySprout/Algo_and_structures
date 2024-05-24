class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.value = value
        self.priority = priority


def get_height(node):
    if node is None:
        return 0
    return node.height


class AVLTree:
    def __init__(self, value, priority):
        self.root = Node(value, priority)

    def is_empty(self):
        return self.root is None

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self.__insert_helper(self.root, value, priority)
        self._restore_balance(self.root)

    def __insert_helper(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
                node.left.parent = node
            else:
                self.__insert_helper(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
                node.right.parent = node
            else:
                self.__insert_helper(node.right, value, priority)

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))
        new_root.height = 1 + max(self.__get_height(new_root.left), self.__get_height(new_root.right))

    def _restore_balance(self, node):
        while node is not None:
            left_height = self.__get_height(node.left)
            right_height = self.__get_height(node.right)
            node.height = 1 + max(left_height, right_height)
            balance = left_height - right_height
            if balance > 1:
                if self.__get_height(node.left.left) >= self.__get_height(node.left.right):
                    self._right_rotate(node)
                else:
                    self._left_rotate(node.left)
                    self._right_rotate(node)
            elif balance < -1:
                if self.__get_height(node.right.right) >= self.__get_height(node.right.left):
                    self._left_rotate(node)
                else:
                    self._right_rotate(node.right)
                    self._left_rotate(node)
            node = node.parent

    @staticmethod
    def __get_height(node):
        if node is None:
            return 0
        return node.height

    def print_tree(self):
        self._print_inorder(self.root)

    def __print_inorder(self, node):
        if node is not None:
            self.__print_inorder(node.left)
            print(f'{node.value}({node.priority})')
            self.__print_inorder(node.right)

    def dequeue(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.left:
            current_node = current_node.left

        deleted_node = (current_node.value, current_node.priority)

        if current_node.parent is None:  # Root node
            if current_node.right:
                self.root = current_node.right
                current_node.right.parent = None
            else:
                self.root = None
        else:
            if current_node.right:
                current_node.parent.left = current_node.right
                current_node.right.parent = current_node.parent
            else:
                current_node.parent.left = None

        self._restore_balance(current_node.parent)
        return deleted_node

    def _print_inorder(self, root):
        pass
