class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class linkedlist:
    def traverse(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
        else:
            print("None")
    def reverse(self,head):
        pre=None 
        curr=head
        nxt=None
        while(curr!=None):
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        head=pre
        return head


        

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=None
obj=linkedlist()
obj.traverse(head)
head=obj.reverse(head)
obj.traverse(head)

