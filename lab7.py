from typing import Any, Callable, Iterable


class TreeNode:
    value: Any
    left_child: 'TreeNode'
    right_child: 'TreeNode'

    def __init__(self, value=None, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.value)

    def add_left(self, child: "TreeNode"):
        self.left_child = child

    def add_right(self, child: "TreeNode"):
        self.right_child = child

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def height(self):
        if self.left_child is None:
            return 0
        if self.right_child is None:
            return 0
        return 1 + max(self.left_child.height(), self.right_child.height())


class BinaryTree:
    root: TreeNode

    def __init__(self, root=None):
        self.root = root

    def height(self):
        if self.root.left_child is None:
            return 0
        if self.root.right_child is None:
            return 0
        return 1 + max(self.root.left_child.height(), self.root.right_child.height())
    

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value: Any):
        def ordered_add(node: TreeNode, value):
            if value < node.value:
                if node.left_child:
                    ordered_add(node.left_child, value)
                else:
                    node.left_child = TreeNode(value)
            else:
                if node.right_child is None:
                    node.add_right(TreeNode(value))
                else:
                    ordered_add(node.right_child, value)

        if self.root is None:
            self.root = TreeNode(value)
        else:
            ordered_add(self.root, value)

    def to_tree(self, elements: Iterable):
        for element in elements:
            self.add(element)

    def search(self, value) -> bool:
        def traverse_pre_order(node, val):
            if node is None:
                return False
            if node.value == val:
                return True
            if val < node.value:
                return traverse_pre_order(node.left_child, val)
            else:
                return traverse_pre_order(node.right_child, val)

        return traverse_pre_order(self.root, value)


H = TreeNode("H")
I = TreeNode("I")
D = TreeNode("D", H, I)
J = TreeNode("J")
E = TreeNode("E", J)
B = TreeNode("B", D, E)
K = TreeNode("K")
F = TreeNode("F", K)
C = TreeNode("C", F, TreeNode("G"))
A = TreeNode("A", B, C)
in_order = []
A.traverse_in_order(in_order.append)
assert [x.value for x in in_order] == ["H", "D", "I", "B", "J", "E", "A", "K", "F", "C", "G"]
pre_order = []
A.traverse_pre_order(pre_order.append)
assert [x.value for x in pre_order] == ["A", "B", "D", "H", "I", "E", "J", "C", "F", "K", "G"]
post_order = []
A.traverse_post_order(post_order.append)
assert [x.value for x in post_order] == ["H", "I", "D", "J", "E", "B", "K", "F", "G", "C", "A"]
my_tree = BinaryTree()
assert my_tree.root == None
my_tree.root = A
assert my_tree.height() == 3
#my_tree.show()
search_tree = BinarySearchTree()
assert search_tree.root == None
assert search_tree.search(0) == False
search_tree.to_tree([4, 3, 8, -1, 5, 1, 9, 10, 2])
#search_tree.show()
pre_order = []
search_tree.root.traverse_pre_order(pre_order.append)
assert [x.value for x in pre_order] == [4, 3, -1, 1, 2, 8, 5, 9, 10]
assert search_tree.search(2) == True
assert search_tree.search(4) == True
assert search_tree.search(5) == True
assert search_tree.search(10) == True
assert search_tree.search(-1) == True
assert search_tree.search(-5) == False
assert search_tree.search(7) == False
assert search_tree.search(100) == False
