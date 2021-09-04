class Node():
    def __init__(self , data ):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None :
                current_node = current_node.next
            current_node.next = Node(value)
    def show_elements(self):
        current_element = self.head
        while current_element is not None:
            print(current_element.data)
            current_element = current_element.next
    def get_element(self,pos):
        index = 0 
        current_element = self.head
        while current_element is not None:
            if index == pos:
                return current_element.data
            current_element = current_element.next
            index += 1
        return "Out of index"
    def insert(self,pos,value):
        node_to_be_inserted = Node(value)
        current_element = self.head
        if self.head is None:
            self.head = node_to_be_inserted
            return "Element Inserted"
        if pos == 0 :
            node_to_be_inserted.next = current_element
            self.head = node_to_be_inserted
            return "Element Inserted"
        else:
            index = 0 
            while current_element is not None:
                if index == pos-1 :
                    node_to_be_inserted.next = current_element.next
                    current_element.next = node_to_be_inserted
                    return "Element Inserted"
                current_element = current_element.next
                index +=1

list1 = LinkedList()
list1.append(2)
list1.append(3)
list1.append(5)
list1.append(7)
list1.append(9)
list1.show_elements()
print("##############")
print(list1.get_element(3))
print("##############")
list1.insert(3,10)
list1.show_elements()