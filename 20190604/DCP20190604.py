# node class for standard linked list
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# linked list class
class linkedList:
    def __init__(self):
        self.head = Node()

    # technically just adds order id to end of linked list
    def record(self, order_id):
        # create new node with order_id data
        newNode = Node(order_id)

        # base case if linked list is empty
        if self.head is None:
            self.head = newNode
            return

        # otherwise find head of linked list
        laste = self.head

        # traverse through linked list until you found last value
        while(laste.next):
            laste = laste.next

        # attached order_id node to end of linked list
        laste.next = newNode

    # get last ith item (technically cheated because I also used data size N)
    def get_last(self, i, N):
        # find head of linked list
        val = self.head

        # base case just in case i is N, returns head
        if i == N:
            return val

        # runs through linked list until point N-i (which is ith last node)
        for j in range(0:N-i):
            val = val.next

        # returns ith last node
        return val

