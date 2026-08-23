// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node {
    int val;
    Node next;
    Node() {}
    Node(int val) { this.val = val; }
    Node(int val, Node next) { this.val = val; this.next = next; }
}

class Solution {
    public Node insert(Node head, int insertVal) {
        Node node = new Node(insertVal);
        if (head == null) {
            node.next = node;
            return node;
        }
        Node cur = head;
        while (cur.next != null && cur.next != head) cur = cur.next;
        cur.next = head;
        Node prev = head, curr = head.next;
        while (true) {
            if (prev.val <= insertVal && insertVal <= curr.val) break;
            if (prev.val > curr.val && (insertVal >= prev.val || insertVal <= curr.val)) break;
            prev = curr;
            curr = curr.next;
            if (prev == head) break;
        }
        prev.next = node;
        node.next = curr;
        return head;
    }
}
