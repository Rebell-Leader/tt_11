class Item():
    def __init__(self, next_node=None, prev_node=None, data=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = data

class linkedlist():
    def __init__(self, node):
        assert isinstance(node, Item)
        self.first_node = node
        self.last_node = node

