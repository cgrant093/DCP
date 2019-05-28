# node/tree class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalTree(node, j):
    # if no children exist, then its a unival tree
    if (node.left is None) and (node.right is None):
        return 1

    # if one child exists and it has same value as parent, then its a unival tree
    elif (node.left is None) and (node.val == node.right.val):
        return 1

    elif (node.right is None) and (node.val == node.left.val):
        return 1

    # cases when two children exist
    else:
        # count unival trees of children
        j = countUnivalTree(node.left, j) + countUnivalTree(node.right, j)

        # if both nodes exist and both are same as parent, then unival tree
        if (node.val == node.right.val) and (node.val == node.left.val):
            j += 1

        return j

tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print("Number of universal value trees is ", countUnivalTree(tree, 0))