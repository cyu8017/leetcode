// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

public class ListNode { public int val; public ListNode next; public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; } }
public class Solution {
    public ListNode InsertionSortList(ListNode head) {
        var dummy = new ListNode();
        while (head != null) {
            var next = head.next; var previous = dummy;
            while (previous.next != null && previous.next.val < head.val) previous = previous.next;
            head.next = previous.next; previous.next = head; head = next;
        }
        return dummy.next;
    }
}