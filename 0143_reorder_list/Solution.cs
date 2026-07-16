// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

public class ListNode { public int val; public ListNode next; public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; } }
public class Solution {
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null) return;
        var slow = head; var fast = head;
        while (fast.next != null && fast.next.next != null) { slow = slow.next; fast = fast.next.next; }
        var second = slow.next; slow.next = null; ListNode previous = null;
        while (second != null) { var next = second.next; second.next = previous; previous = second; second = next; }
        var first = head; second = previous;
        while (second != null) {
            var firstNext = first.next; var secondNext = second.next;
            first.next = second; second.next = firstNext; first = firstNext; second = secondNext;
        }
    }
}