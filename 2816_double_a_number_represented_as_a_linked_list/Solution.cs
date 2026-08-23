// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode DoubleIt(ListNode head) {
        ListNode Rev(ListNode node) {
            ListNode prev = null;
            while (node != null) {
                ListNode nxt = node.next;
                node.next = prev;
                prev = node;
                node = nxt;
            }
            return prev;
        }
        head = Rev(head);
        int carry = 0;
        ListNode cur = head, prev2 = null;
        while (cur != null) {
            int val = cur.val * 2 + carry;
            cur.val = val % 10;
            carry = val / 10;
            prev2 = cur;
            cur = cur.next;
        }
        if (carry > 0) prev2.next = new ListNode(carry);
        return Rev(head);
    }
}
