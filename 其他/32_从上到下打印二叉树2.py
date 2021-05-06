# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  32_从上到下打印二叉树2.py.py
# 当前系统日期时间：2020/7/11，15:12 
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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


if __name__ == '__main__':
    # [3,9,20,null,null,15,7]
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    s = Solution()
    print(s.levelOrder(t1))
