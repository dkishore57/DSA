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
    def addatfront(self,head):
        head.next=n1
        return head
    def addatlast(self,head,val):
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=val
        return head
    def addatindex(self,head,val,index):
        temp=head
        count=0
        while(count!=index-1):
            temp=temp.next
            count+=1
        val.next=temp.next
        temp.next=val
        return head
    def removeatfront(self,head):
        head=head.next
        return head
    def removeatlast(self,head):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        return head
    def removeatindex(self,head,index):
        temp=head
        count=0
        while(count!=index-1):
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return head
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
obj=linkedlist()
print("LINKED LIST CREATED")
obj.traverse(head)
print("0 ADDED AT FRONT")
head=obj.addatfront(Node(0))
obj.traverse(head)
print("7 ADDED AT LAST")
head=obj.addatlast(head,Node(7))
obj.traverse(head)
print("REVERSED")
head=obj.reverse(head)
obj.traverse(head)
print("18 ADDED AT INDEX 2")
head=obj.addatindex(head,Node(18),2)
obj.traverse(head)
print("FIRST INDEX REMOVED")
head=obj.removeatfront(head)
obj.traverse(head)
print("LAST INDEX REMOVED")
head=obj.removeatlast(head)
obj.traverse(head)
print("REMOVED INDEX 2")
head=obj.removeatindex(head,1)
obj.traverse(head)

