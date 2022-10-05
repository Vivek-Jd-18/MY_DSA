class Node:
    def __init__(_, data=None, next=None):
        _.data = data
        _.next = next


class data:
    ls = [1, 2, 3, 4, 5, 6]
    ll = []

    for i in ls:
        ll.append(Node(i, i+1))

    def __repr__(_):
        st=''
        for i in range(len(_.ll)):
            st+= str(i) + "-->"
        return st
    def ret (_):
        return _.ls[2].next

n = data()
print(n)
print(n.ret())