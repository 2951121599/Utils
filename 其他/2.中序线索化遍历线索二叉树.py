# -*-coding:gbk-*-
class TreeNode(object):
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None
        # 新增类型指针
        # 规定：
        # 如果left_type==0 表示指向的是左子树，如果是1 则表示指向前驱结点
        # 如果right_type==0 表示指向的是右子树，如果是1 怎表示指向后继结点
        self.left_type = 0
        self.right_type = 0


class ThreadedBinaryTree(object):
    def __init__(self):
        self.root = None
        # 在递归进行线索化，总是保留前一个结点
        self.pre = None  # 为实现线索化，需要创建给指向当前结点的前驱结点指针

    # 中序遍历线索化二叉树
    def threaded_in_order(self, node):
        if node is None:
            return
        temp_node = node
        while temp_node:
            # 循环的找到left_type=1的结点，第一个找到就是值为8的结点
            # 后面随着遍历而变化，因为当left_type=1时，说明该结点是按照线索化处理后的有效结点
            while temp_node.left_type == 0:  # 从根结点开始向左找，找到第一个1停止
                temp_node = temp_node.left
            # 打印当前这个结点
            print(temp_node.val, end=" ")
            # 如果当前结点的右指针指向的是后继结点，就一直输出
            while temp_node.right_type == 1:
                # 获取到当前结点的后继结点
                temp_node = temp_node.right
                print(temp_node.val, end=" ")
            # 如果不等于1了，就替换这个遍历的结点
            temp_node = temp_node.right

    # 二叉树进行中序线索化的方法
    def threaded_node(self, node):  # node: 就是当前需要线索化的结点
        if node is None:
            return
        # 先线索化左子树
        self.threaded_node(node.left)
        # 线索化当前结点

        # 处理当前结点的前驱结点
        if node.left is None:  # 如果当前结点左子结点为空
            node.left = self.pre  # 让当前结点的左指针指向前驱结点
            node.left_type = 1  # 修改当前结点的左指针类型 为 前驱结点

        # 处理当前结点的后继结点
        if self.pre and self.pre.right is None:
            self.pre.right = node  # 让前驱结点的右指针指向当前结点
            self.pre.right_type = 1  # 修改前驱结点的右指针类型
        self.pre = node  # 每处理一个结点后，让当前结点是下一个结点的前驱结点
        # 线索化右子树
        self.threaded_node(node.right)


if __name__ == '__main__':
    # 调用add 自动创建结点
    t = ThreadedBinaryTree()

    # 手动创建结点--只是为了更好测试线索化有没有成功
    root = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    root.left = t2
    root.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    # 线索化二叉树
    t.threaded_node(root)
    # print("线索化二叉树的中序遍历结果为：")
    t.threaded_in_order(root)
