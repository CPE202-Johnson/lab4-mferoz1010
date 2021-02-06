class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __eq__(self, other):
        if type(self) == type(other):
            return self.item == other.item

    def __lt__(self, other):
        if type(self) == type(other):
            return self.item < other.item


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None
        self.tail = None

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head:
            return False
        else:
            return True

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        temp = Node(item)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            current = self.head
            while current:
                if temp < self.head:
                    temp.next = current
                    current.prev = temp
                    self.head = temp
                elif self.tail < temp:
                    self.tail.next = temp
                    temp.prev = self.tail
                    self.tail = temp
                else:
                    if current < temp < current.next:
                        current.next.prev = temp
                        temp.next = current.next
                        current.next = temp
                        temp.prev = current
                current = current.next

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        temp = Node(item)
        if self.is_empty():
            return False
        else:
            current = self.head
            while current.next:
                if temp == self.head:
                    self.head.next.prev = None
                    self.head = self.head.next
                elif temp == self.tail:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                else:
                    if temp == current:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                current = current.next
            return True

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        temp = Node(item)
        index = 0
        if self.is_empty():
            return None
        else:
            current = self.head
            while current:
                if temp == self.head:
                    return index
                else:
                    if not(temp == current):
                        current = current.next
                        index += 1
                    else:
                        return index
            return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        count = 0
        if index < 0 or index >= self.size():
            raise IndexError
        else:
            current = self.head
            count = 0
            while current:
                if count == index:
                    self.remove(current.item)
                    return current.item
                else:
                    count += 1
                    current = current.next

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        temp = Node(item)
        check = False
        if self.is_empty():
            return check
        else:
            current = self.head
            if current == temp:
                return True
            else:
                ord_lst = OrderedList()
                ord_lst.tail = current.next
                ord_lst.head = self.head
                return ord_lst.search(item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        new_lst = []
        if self.is_empty():
            return new_lst
        else:
            current = self.head
            while current:
                new_lst.append(current.item)
                current = current.next
            return new_lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        rev_lst = []
        if self.is_empty():
            return rev_lst
        else:
            current = self.tail
            rev_lst.append(current.item)
            if current.prev:
                current = current.prev
                ord_lst = OrderedList()
                ord_lst.tail = current
                ord_lst.head = self.head
                rev_lst.extend(ord_lst.python_list_reversed())
            return rev_lst

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty():
            return 0
        current = self.head
        if current:
            return 1
        else:
            self.head = self.head.next
            lst_size = self.size() + 1
            self.head = current
            return lst_size

