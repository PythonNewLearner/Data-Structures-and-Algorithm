# -*- coding: utf-8 -*-
"""
Created on Thu May 23 03:26:48 2019

@author: Bai Chen
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insertStart(self, data):  # insert data at beginnning of the list
        self.size += 1
        newNode = Node(data)
        if not self.head:  # the head is None
            self.head = newNode
        else:  # the head is not None
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self):
        if self.head is None:
            return

        self.size-=self.size

        currentNode=self.head
        previousNode=None

        while currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode=currentNode.nextNode

    # O(1)
    def size(self):
        return self.size

    # O(N)
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    # O(N)
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

a=LinkedList()
a.insertStart(3)
a.insertStart(4)
a.insertEnd(5)
print(a.traverseList())
a.size()

