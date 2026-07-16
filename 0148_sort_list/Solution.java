// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

class ListNode { int val; ListNode next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val, ListNode next) { this.val = val; this.next = next; } }
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode slow = head, fast = head, prev = null;
        while (fast != null && fast.next != null) { prev = slow; slow = slow.next; fast = fast.next.next; }
        prev.next = null;
        return merge(sortList(head), sortList(slow));
    }
    private ListNode merge(ListNode left, ListNode right) {
        ListNode dummy = new ListNode(), tail = dummy;
        while (left != null && right != null) {
            if (left.val <= right.val) { tail.next = left; left = left.next; } else { tail.next = right; right = right.next; }
            tail = tail.next;
        }
        tail.next = left != null ? left : right;
        return dummy.next;
    }
}