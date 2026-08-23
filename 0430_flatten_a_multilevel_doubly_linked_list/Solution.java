// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
}

class Solution {
    public Node flatten(Node head) {
        Node current = head;
        while (current != null) {
            if (current.child != null) {
                Node nextNode = current.next;
                Node childHead = flatten(current.child);
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
