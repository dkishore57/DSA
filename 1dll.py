"""
1.introduction to linked list,learn about struct,and how is node represented.
2.inserting a node in linked list
3.deleting a node in linkedlist
4.find the length of the linked[learn traversal]
5.search an element in the ll 
6.middle of a linked list[tortoisehare method]
7.reverse a linked list[iterative]
8.reverse a ll[recursive]
9.detect a loop in ll
10.find the starting point in ll
11.length of loop in ll
12.check if ll is palindrome or not
13.seggrregate odd and even nodes in ll
14.remove nth node from the back of the ll
15.delete the middle node of ll
16.sort ll
17.sort a ll of 0's 1's and 2's by changing links
18.find the intersection point of y ll
19.add 1 to a number represented by ll
20.add 2 nmbers in ll
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def traverse(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
        print("None")
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
head=n1
obj=linkedlist()
obj.traverse(head)