// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) {
            return head;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode before = dummy;
        for (int i = 0; i < left - 1; i++) {
            before = before.next;
        }

        ListNode start = before.next;
        ListNode current = start.next;

        for (int i = 0; i < right - left; i++) {
            start.next = current.next;
            current.next = before.next;
            before.next = current;
            current = start.next;
        }

        return dummy.next;
    }
}
