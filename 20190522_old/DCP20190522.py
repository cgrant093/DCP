#Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#serialize function
def serialize(node):
    serial = "";

    if node:
        serial += node.val + " " + serialize(node.left) + serialize(node.right)
    else:
        serial += "# "

    return serial

#deserialize function
def deserialize(treeInWords):

    #defines decoding leaves
    def decode(leaves):
        leaf = next(leaves)

        if leaf == "#":
            return None

        node = Node(leaf)
        node.left = decode(leaves)
        node.right = decode(leaves)

        return node

    #splits into array
    leaves = iter(treeInWords.split(" "))
    return decode(leaves)

node = Node('root', Node('left', Node('left.left')), Node('right'))
#print(node)
#print(serialize(node))
#print(deserialize(serialize(node)))
#print(serialize(deserialize(serialize(node))))

print(deserialize(serialize(node)).left.left.val == 'left.left')