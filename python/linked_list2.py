# most of the linked list's features are implemented in this code
class Node:
    """
    main(every wether it is head node, normal node or last node ) node creation happens here.
    """
    def __init__(_, data=None, next=None):
        _.data = data
        _.next = next


class link:

    def __init__(_):
        _.head = None

    def insert_begin(_, data):
        """
        inserting a node at initial position(head position).
        """
        node = Node(data, _.head)
        _.head = node

    def print(_):
        """
        prints a whole linked list.
        """
        if _.head is None:
            print("Linked List is Empty.! ")
            return

        itr = _.head
        listr = ''

        while itr:
            if itr.next != None:
                listr += str(itr.data) + "-->"
                itr = itr.next
            else:
                listr += str(itr.data) + ""
                itr = itr.next

        print(listr)

    def insert_end(_, data):
        """
        inserts an element at the end of list(last node).
        """
        if _.head == None:
            _.head = Node(data, None)
            return

        itr = _.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_len(_):
        """
        returns how many nodes are presents there in a list.
        """
        count = 0
        itr = _.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(_, index):
        """
        removes an element specified at specific location.
        """
        if index < 0 or index > _.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            _.head = _.head.next
            return

        count = 0
        itr = _.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_in(_, index, data):
        """
        inserts an element at specified location in the list.
        """
        if index < 0 or index > _.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            _.insert_begin(data)
            return

        count = 0
        itr = _.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1
