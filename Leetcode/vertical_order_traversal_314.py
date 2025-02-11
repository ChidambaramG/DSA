from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Leetcode 314
# Do BFS and subtract level if left and add levels if right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        vertical_order = defaultdict(list)
        vertical_order[0] = [root.val]
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level-1))
                vertical_order[level-1].append(node.left.val)
            if node.right:
                queue.append((node.right, level+1))
                vertical_order[level+1].append(node.right.val)
            
        return [vertical_order[x] for x in sorted(vertical_order.keys())]

        
