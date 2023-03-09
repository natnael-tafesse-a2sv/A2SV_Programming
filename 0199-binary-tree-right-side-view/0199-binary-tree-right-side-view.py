# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        ans = []
        x = 1
        while queue:
            temp1 = []
            count = x
            x = 0
            while count > 0:
                if queue:
                    temp = queue.popleft()
                if count ==1:
                    temp1.append(temp.val)
                count -= 1
                if temp.left:
                    queue.append(temp.left)
                    x += 1
                if temp.right:
                    x += 1
                    queue.append(temp.right)
                                
            ans.extend(temp1)
        return ans