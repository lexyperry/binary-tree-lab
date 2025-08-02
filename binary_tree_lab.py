from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1
    

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val and  q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else: 
        return root
