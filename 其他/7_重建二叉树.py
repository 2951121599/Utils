class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            # 先建立根节点
            tree = TreeNode(preorder[0])
            # 递归
            # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
            i = inorder.index(preorder[0])
            # 中左 中右
            zz, zy = inorder[:i], inorder[i + 1:]
            # 前左 前右
            qz, qy = preorder[1:i + 1], preorder[i + 1:]

            tree.left = self.buildTree(qz, zz)
            tree.right = self.buildTree(qy, zy)
        return tree


if __name__ == '__main__':
    s = Solution()
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]

    print(s.buildTree(preorder, inorder))
