// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode SortLinkedList(ListNode head) {
        if (head == null) return null;
        ListNode prev = head, cur = head.next;
        while (cur != null) {
            if (cur.val < 0) {
                prev.next = cur.next;
                cur.next = head;
                head = cur;
                cur = prev.next;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
        return head;
    }
}
