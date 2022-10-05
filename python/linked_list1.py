# incomplete , work in progress
class Node:
    '''
    initializing data and next_node
    '''
    data = None
    next_node = None

    def __init__(_, data):
        _.data = data

    def __repr__(_):
        return f"data is {_.data}"


class linked_list:
    def __init__(_):
        _.head = None

    def isEmpty(_):
        return _.head == None

    def size(_):
        current = _.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(_, data):
        new_node = Node(data)
        new_node.next_node = _.head
        _.head = new_node

    def search(_, key):
        current = _.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(_, data, index):
        """
        Insert a new Node containing a data at index position 
        Insertion takes O(1) time but finding the node at the 
        insertion point takes O(n) time.

        Takes overall O(n) time.
        """
        if index == 0:
            _.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = _.head

            while position > 1:
                current = new.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node 

    def __repr__(_):
        '''
        returns a string representation of list , Takes O(n) time 😃
        '''
        nodes = []
        current = _.head

        while current:
            if current is _.head:
                nodes.append("[Head: [%s]]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: [%s]]" % current.data)
            else:
                nodes.append("[[%s]]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)
