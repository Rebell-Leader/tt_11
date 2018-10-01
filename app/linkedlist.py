def multiply(a, b)
метод добавления, метод удаления, метод, возвращающий элемент, двусвязный список

//
class ListNode:  
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None

        self.prev = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
