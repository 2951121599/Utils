# -*-coding:gbk-*-

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        TinIndex = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:TinIndex + 1], tin[0:TinIndex])
        root.right = self.reConstructBinaryTree(pre[TinIndex + 1:], tin[TinIndex + 1:])
        return root

    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res

    def PostTraversal(self, root):  # 后序遍历
        if root != None:
            self.PostTraversal(root.left)
            self.PostTraversal(root.right)
            print(root.val)


pre = [1, 2, 4, 5, 3, 6, 7]
tin = [4, 2, 5, 1, 6, 3, 7]
S = Solution()
root = S.reConstructBinaryTree(pre, tin)
print(S.levelOrder(root))
