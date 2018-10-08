'''
def multiply(a, b)
метод добавления, метод удаления, метод, возвращающий элемент, двусвязный список

//
class ListNode:  
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.elem = elem

        # store reference (next item)
        self.next_item = None

        self.prev_item = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
    def elem():
'''
class Item():
    def __init__(self, next_node=None, previous_node=None, data=None):
        self.next_item = next_node
        self.prev_item = previous_node
        self.item = data



class LinkedList():
    def __init__(self, node):
        assert isinstance(node, Item)
        self.first_node = node
        self.last_node = node

    def push(self, node):
        '''Pushes the node <node> at the "front" of the ll
        '''
        node.next_node = self.first_node
        node.previous_node = None
        self.first_node.previous_node = node
        self.first_node = node

    def pop(self):
        '''Pops the last node out of the list'''
        old_last_node = self.last_node
        to_be_last = self.last_node.prev_item
        to_be_last.next_node = None
        old_last_node.prev_item = None

        # Set the last node to the "to_be_last"
        self.previous_node = to_be_last

        return old_last_node

    def remove(self, node):
        '''Removes and returns node, and connects the previous and next
        nicely
        '''
        next_node = node.next_node
        previous_node = node.previous_node

        previous_node.next_node = next_node
        next_node.previous_node = previous_node

        # Make it "free"
        node.next_node = node.previous_node = None

        return node

    def __str__(self):
        next_node = self.first_node
        s = ""
        while next_node:
            s += "--({:0>2d})--\n".format(next_node.item)
            next_node = next_node.next_item

        return s

        return


node1 = Item(data=1)

linked_list = LinkedList(node1)


for i in range(10):
    if i == 5:
        node5 = Item(data=5)
        linked_list.push(node5)
    else:
        linked_list.push(Item(data=i))

print (linked_list)

print ("pop method")
print (linked_list.pop().item)

print ("\n\n")
print (linked_list)


print ("\n\n")
linked_list.push(Item(data=10))

print ("\n\n")
print (linked_list)


linked_list.remove(node5)

print ("\n\n")
print (linked_list)