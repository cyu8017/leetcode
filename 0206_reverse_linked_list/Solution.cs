// LeetCode 0206 - Reverse Linked List\n// https://leetcode.com/problems/\n\npublic class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode ReverseList(ListNode head) {
        ListNode previous = null;
        while (head != null) { var next = head.next; head.next = previous; previous = head; head = next; }
        return previous;
    }
}
