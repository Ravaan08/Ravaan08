class Node:
    def __init__(self, item=None, nxt=None):
        self.item = item
        self.nxt = nxt


class Start:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_first(self, item):
        new_node = Node(item, self.head)
        self.head = new_node

    def insert_at_last(self, item):
        self.new_node = Node(item)
        if not self.is_empty():
            self.temp = self.head
            while self.temp.nxt is not None:
                self.temp = self.temp.nxt
            self.temp.nxt = self.new_node
        else:
            self.head = self.new_node

    def insert_at_position(self, item, position):
        self.new_node = Node(item)
        count = 0
        if not self.is_empty():
            self.temp = self.head
            while self.temp.nxt is not None:
                count += 1
                if count == position-1:
                    self.new_node.nxt = self.temp.nxt
                    self.temp.nxt = self.new_node
        else:
            self.temp = self.new_node

    def search_at_item(self,item):
        if not self.is_empty():
            self.temp = self.head
            while self.temp.nxt is not None:
                if self.temp.item is item:
                    return "is available"
                self.temp = self.temp.nxt
            return None
        else:
            return None

    def search_at_position(self,position):
        self.temp = self.head
        count = 0
        if self.is_empty() is not None:
            while self.temp.nxt is not None:
                count += 1
                if count is position-1:
                    print(self.temp.item)
                    break
                self.temp = self.temp.nxt
            print("There is no position at "+str(position))
        else:
            return None

    def delete_at_first(self):
        if not self.is_empty():
            self.temp = self.head
            self.head = self.temp.nxt

    def delete_at_last(self):
        if not self.is_empty():
            self.temp = self.head
            while self.temp.nxt != None:
                self.temp = self.temp.nxt
                if self.temp.nxt.nxt==None:
                    self.temp.nxt=None
                    break

    def delete_at_position(self,position):
        if not self.is_empty():
            self.temp = self.head
            count = 0
            while self.temp.nxt is not None:
                count += 1
                if count is position-1 and self.temp.nxt.nxt is not None:
                    self.temp.nxt = self.temp.nxt.nxt
                    break
                self.temp = self.temp.nxt
            else:
                self.temp = None
        else:
            return "There is no element in SLL"

    def traverse(self):
         if not self.is_empty():
            self.temp = self.head
            while self.temp.nxt is not None:
                print(self.temp.item,end=" ")
                self.temp = self.temp.nxt
            else:
                print(self.temp.item)
         else:
             print(self.temp.item)

'''driving class'''
s1 = Start()
s1.insert_at_first(20)
s1.insert_at_first(10)
s1.insert_at_last(30)
s1.insert_at_last(40)
s1.insert_at_last(50)
s1.delete_at_last()
s1.delete_at_last()
s1.traverse()

