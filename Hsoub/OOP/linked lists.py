class node:
    nodes = 0

    def __init__(self, Data):
        
        self.Data = Data
        self.next = None

        node.nodes += 1
        

class linkedLists :

    def __init__(self):

        self.head = None

    def PrintList (self):
        items = []
        item = self.head

        while(item):
            items.append (item.Data)
            item = item.next
        else : print (items)


    def push (self , data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode


    def append(self, data):
        newNode = node(data)
        last = LLS.head

        while last.next:
            last = last.next

        last.next = newNode
    
    def insert (self ,prevNode ,data):

        
            newNode = node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode
    
    def replace(self, replaced, data):
        if replaced is None:
            return  # Handle the case where 'replaced' is not found
    
        replaced.Data = data
    
    def delete(self, Node):
        next_node = Node.next
        if (Node.next == None):
            Node = None

        next_node = Node.next
        Node.Data = next_node.Data
        Node.next = next_node.next
        next_node = None



        

    

LLS = linkedLists()

node1 = node(1)
node2  = node(2)
node4 = node(4)


LLS.head = node1
LLS.head.next = node2
node2.next = node4

LLS.push(0)
LLS.append(5)
LLS.insert(node2,3)
LLS.replace(node1 , 6)
LLS.delete(node2)

LLS.PrintList()