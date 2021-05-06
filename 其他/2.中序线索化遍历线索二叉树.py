# -*-coding:gbk-*-
class TreeNode(object):
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None
        # ��������ָ��
        # �涨��
        # ���left_type==0 ��ʾָ������������������1 ���ʾָ��ǰ�����
        # ���right_type==0 ��ʾָ������������������1 ����ʾָ���̽��
        self.left_type = 0
        self.right_type = 0


class ThreadedBinaryTree(object):
    def __init__(self):
        self.root = None
        # �ڵݹ���������������Ǳ���ǰһ�����
        self.pre = None  # Ϊʵ������������Ҫ������ָ��ǰ����ǰ�����ָ��

    # �������������������
    def threaded_in_order(self, node):
        if node is None:
            return
        temp_node = node
        while temp_node:
            # ѭ�����ҵ�left_type=1�Ľ�㣬��һ���ҵ�����ֵΪ8�Ľ��
            # �������ű������仯����Ϊ��left_type=1ʱ��˵���ý���ǰ�����������������Ч���
            while temp_node.left_type == 0:  # �Ӹ���㿪ʼ�����ң��ҵ���һ��1ֹͣ
                temp_node = temp_node.left
            # ��ӡ��ǰ������
            print(temp_node.val, end=" ")
            # �����ǰ������ָ��ָ����Ǻ�̽�㣬��һֱ���
            while temp_node.right_type == 1:
                # ��ȡ����ǰ���ĺ�̽��
                temp_node = temp_node.right
                print(temp_node.val, end=" ")
            # ���������1�ˣ����滻��������Ľ��
            temp_node = temp_node.right

    # ���������������������ķ���
    def threaded_node(self, node):  # node: ���ǵ�ǰ��Ҫ�������Ľ��
        if node is None:
            return
        # ��������������
        self.threaded_node(node.left)
        # ��������ǰ���

        # ����ǰ����ǰ�����
        if node.left is None:  # �����ǰ������ӽ��Ϊ��
            node.left = self.pre  # �õ�ǰ������ָ��ָ��ǰ�����
            node.left_type = 1  # �޸ĵ�ǰ������ָ������ Ϊ ǰ�����

        # ����ǰ���ĺ�̽��
        if self.pre and self.pre.right is None:
            self.pre.right = node  # ��ǰ��������ָ��ָ��ǰ���
            self.pre.right_type = 1  # �޸�ǰ��������ָ������
        self.pre = node  # ÿ����һ�������õ�ǰ�������һ������ǰ�����
        # ������������
        self.threaded_node(node.right)


if __name__ == '__main__':
    # ����add �Զ��������
    t = ThreadedBinaryTree()

    # �ֶ��������--ֻ��Ϊ�˸��ò�����������û�гɹ�
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
    # ������������
    t.threaded_node(root)
    # print("������������������������Ϊ��")
    t.threaded_in_order(root)
