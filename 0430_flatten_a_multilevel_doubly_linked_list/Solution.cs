// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
    public Node(int val = 0, Node prev = null, Node next = null, Node child = null) {
        this.val = val;
        this.prev = prev;
        this.next = next;
        this.child = child;
    }
}

public class Solution {
    public Node Flatten(Node head) {
        Node current = head;
        while (current != null) {
            if (current.child != null) {
                Node nextNode = current.next;
                Node childHead = Flatten(current.child);
                current.next = childHead;
                childHead.prev = current;
                Node tail = childHead;
                while (tail.next != null) {
                    tail = tail.next;
                }
                tail.next = nextNode;
                if (nextNode != null) {
                    nextNode.prev = tail;
                }
                current.child = null;
            }
            current = current.next;
        }
        return head;
    }
}
