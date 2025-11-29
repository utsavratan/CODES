public class MyLinkedList {
    ListNode head=null;

    void insertAtBegin (int val) {
        ListNode newNode= new ListNode(val);
        newNode.next=head;
        head=newNode;
    }
}
class ListNode {
    int data;
    ListNode next;
    ListNode(int val) {
        data=val;
        next=null;
    }
}
