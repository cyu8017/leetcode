// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

public class ListNode { public int val; public ListNode next; public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; } }
public class Solution {
    public ListNode SortList(ListNode head) {
        if (head == null || head.next == null) return head;
        var slow = head; var fast = head; ListNode previous = null;
        while (fast != null && fast.next != null) { previous = slow; slow = slow.next; fast = fast.next.next; }
        previous.next = null;
        return Merge(SortList(head), SortList(slow));
    }
    private ListNode Merge(ListNode left, ListNode right) {
        var dummy = new ListNode(); var tail = dummy;
        while (left != null && right != null) {
            if (left.val <= right.val) { tail.next = left; left = left.next; } else { tail.next = right; right = right.next; }
            tail = tail.next;
        }
        tail.next = left ?? right;
        return dummy.next;
    }
}