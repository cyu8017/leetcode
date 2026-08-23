// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

class ListNode { int val; ListNode next; ListNode(int x) { val = x; } }
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) { slow = slow.next; fast = fast.next.next; }
        ListNode second = slow.next; slow.next = null; ListNode prev = null;
        while (second != null) { ListNode next = second.next; second.next = prev; prev = second; second = next; }
        ListNode first = head; second = prev;
        while (second != null) {
            ListNode firstNext = first.next, secondNext = second.next;
            first.next = second; second.next = firstNext; first = firstNext; second = secondNext;
        }
    }
}