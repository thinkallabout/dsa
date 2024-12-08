"""Implementation of a binary tree.

Child nodes are enforced to be in the correct order for a binary search
tree. This is not a self-balancing tree."""

# TODO: fill(), compute height, level, depth (this may come forward into n-ary tree).
# TODO: self balancing.

from typing import Optional

class TreeNode:
    def __init__(self, 
                 value: int,
                 left_child: Optional['TreeNode'] = None, 
                 right_child: Optional['TreeNode'] = None):
        self.value = value
        self._left_child = None
        self._right_child = None
        if left_child:
            self.left_child = left_child
        if right_child:
            self.right_child = right_child

    def search(self, value: int) -> bool:
        if self.value == value:
            return True
        if self.left_child and value < self.value:
            return self.left_child.search(value)
        if self.right_child and value > self.value:
            return self.right_child.search(value)
        return False

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, child: 'TreeNode'):
        if child.value > self.value:
            raise ValueError(f"left child value {child.value} is more then {self.value}")
        self._left_child = child

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, child: 'TreeNode'):
        if child.value < self.value:
            raise ValueError(f"right child value {child.value} is less then {self.value}")
        self._right_child = child


def _create_complete_tree(size: int) -> TreeNode:
    """Create a complete binary tree.
    
    Args:
        size: Number of nodes in the final tree.
    Returns:
        The root node.
    """
    # TODO(cameron): Implement this.
    pass


if __name__ == '__main__':
    root = TreeNode(2)
    root.left_child = TreeNode(1)
    root.right_child = TreeNode(3, right_child=TreeNode(4))
    print(f'Found 4: {root.search(4)}')