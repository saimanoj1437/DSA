# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        prev,storing  = None,float("inf")

        def inorder(node):

            nonlocal prev,storing
        

            if node is None:
                return 

            inorder(node.left)

            if prev is not None:

                storing = min(storing, node.val - prev.val)

            prev = node

            inorder(node.right)

        inorder(root)

        return storing

    
        
        