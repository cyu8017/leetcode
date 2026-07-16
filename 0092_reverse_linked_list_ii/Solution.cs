// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode ReverseBetween(ListNode head, int left, int right) {
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
