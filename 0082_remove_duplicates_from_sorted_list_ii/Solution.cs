// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        var dummy = new ListNode(0, head);
        var previous = dummy;

        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                previous.next = head.next;
            } else {
                previous = previous.next;
            }
            head = head.next;
        }

        return dummy.next;
    }
}
