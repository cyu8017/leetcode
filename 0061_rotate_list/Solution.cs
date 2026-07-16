// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode RotateRight(ListNode head, int k) {
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
