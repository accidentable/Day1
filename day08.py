class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class LinkedList:
    
    def __init__(self):
        self.first = None
        
    def append(self, a):
        
        new_Node = Node(a)
        if self.first is None:
            self.first = new_Node
            return
        else:
            curr = self.first
            while curr.nextNode != None: # 마지막 노드 찾기
                curr = curr.nextNode
            curr.nextNode = new_Node
    
    def contains(self,val):

        curr = self.first
        while curr != None:
            if curr.value == val:
                return True
            curr = curr.nextNode
        
        return False
    
    