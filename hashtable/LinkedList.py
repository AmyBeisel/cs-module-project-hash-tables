class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    #runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    #Runtime: 
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    #runtime: O(n) n = number of nodes
    #space complexity: constant O(1)
    def delete(self, value):
        curr = self.head

        #if the value is the head
        if curr.value == value:
            self.head = curr.next
            return curr
        
        #reassign pointers
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                #readdress the pointers
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        return None


    
    #runtime = O(n) n = number of nodes
    def find(self, value):
        curr = self.head
        #loop through the list
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None