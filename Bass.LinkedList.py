#Author: Rachelle Bass
#Date: 5/12/20
#Descrption: LinkedList class that uses recursion in the add and remove contains, insert, and reverse methods
#Also, a recursive method that takes a linked list and returns a regular Python list with the values.

class Node:
    """creates a node for a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """creates and modifies a linked list """
    def __init__(self):
        self._head = None

    def help_add(self, val, new_node):
        """takes value and a node(provided by add function and adds a node containing val to the linked list"""
        if new_node.next is None:           #add node with val when reaching None node
            new_node.next = Node(val)
        else:
            self.help_add(val, new_node.next)  #function calls itself with the next node

    def add(self, val):
        """takes value and adds a node containing val to the linked list with helper fuction"""
        if self._head is None:          #adds val node if list is empty
            self._head = Node(val)
            return
        self.help_add(val, self._head)  #calls help_add function with node value filled in

    def display(self):
        """Prints out the values in the linked list"""
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def help_remove(self, val, previous, current):
        """Removes the node containing val from the linked list"""
        if current is not None and current.data != val:             #continue calling function until val or end of list is met
            self.help_remove(val, previous.next, current.next)
        else:
            previous.next = current.next        #change next to exclude val when found

    def remove(self, val):
        if self._head is None:  #check if list is empty
            return
        if self._head.data == val:          #if val is at head, move head to next node
            self._head = self._head.next
            return
        current = self._head
        self.help_remove(val, current, current.next)    #pass head of list and next node

    def help_contains(self, val, new_node):
        """takes val and node from contains function. returns true if val in linked list and false if otherwise"""
        if new_node.data is val:
            print(True)
            return True
        if new_node.next is None:
            print(False)
            return False
        self.help_contains(val, new_node.next)

    def contains(self, val):
        """takes value. returns true if value in list and false if otherwise"""
        return self.help_contains(val, self._head)

    def help_insert(self,val,pos,current,counter):
        """used with insert function. inserts a node containing val into the linked list at position passed"""
        if current.next is None:        #insert node if end of the list is reached
            current.next = Node(val)
            return

        if counter == (pos-1):      #inserts new node and assigns new and previous next location.
            temp= current.next
            current.next = Node(val)
            current.next.next = temp
            return
        self.help_insert(val,pos,current.next,counter+1)


    def insert(self,val,pos):
        """inserts a node containing val into the linked list at position passed"""
        if self._head is None:      #if list is empty, node is added
            self.add(val)
            return
        if pos == 0:                #if new node is first, adds node and assigns next to previous first in position
            temp= self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            self.help_insert(val,pos,self._head,0)
            return

    def help_reverse(self, current):
        """with reverse function, helps reverse order of nodes"""
        previous = current
        previousNext = current.next
        if current.next is None:
            return
        if current.next is not None:
            replace = self.more_help(current.next)
        self._head = replace
        replace = previousNext
        current = previous
        self.help_reverse(current.next)
        return

    def more_help(self, next):
        if next.next is None:
            return next
        self.more_help(next.next)

    def reverse(self):
        """does not take any parameters. reverses the order of the nodes in the linked list"""
        if self._head is None:
            return
        self.help_reverse(self._head)


    def help_to_regular_list(self, current):
        """with to_regular_list function, helps return a regular python list from linked list"""
        if current is None:             #returns if list is empty or end of list is reached
            return self.result
        self.result +=[current.data]    #adds current node data to python result list
        if current is not None:         #recursion going to next node until end is reached
            self.help_to_regular_list(current.next)

    def to_regular_list(self):
        """returns a regular python list from linked list"""
        self.result = []        #adds new empty list
        self.help_to_regular_list(self._head)
        return  self.result