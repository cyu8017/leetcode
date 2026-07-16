// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode tail = head;
        int length = 1;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        tail.next = head;
        k %= length;
        if (k == 0) {
            tail.next = null;
            return head;
        }

        int steps = length - k;
        ListNode newTail = head;
        for (int i = 0; i < steps - 1; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
