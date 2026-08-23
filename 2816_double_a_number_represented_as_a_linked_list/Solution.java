// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode doubleIt(ListNode head) {
        head = rev(head);
        int carry = 0;
        ListNode cur = head, prev = null;
        while (cur != null) {
            int val = cur.val * 2 + carry;
            cur.val = val % 10;
            carry = val / 10;
            prev = cur;
            cur = cur.next;
        }
        if (carry > 0) prev.next = new ListNode(carry);
        return rev(head);
    }

    private ListNode rev(ListNode node) {
        ListNode prev = null;
        while (node != null) {
            ListNode nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    }
}
