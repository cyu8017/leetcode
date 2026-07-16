// LeetCode 0203 - Remove Linked List Elements\n// https://leetcode.com/problems/\n\npublic class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
        var dummy = new ListNode(0, head);
        var current = dummy;
        while (current.next != null) {
            if (current.next.val == val) current.next = current.next.next;
            else current = current.next;
        }
        return dummy.next;
    }
}
