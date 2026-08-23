// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode sortLinkedList(ListNode head) {
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
