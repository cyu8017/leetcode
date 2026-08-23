// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode[] SplitCircularLinkedList(ListNode list) {
        if (list == null) return new ListNode[] { null, null };
        ListNode slow = list, fast = list;
        while (fast.next != list && fast.next.next != list) {
            slow = slow.next;
            fast = fast.next.next;
        }
        if (fast.next.next == list) fast = fast.next;
        ListNode head2 = slow.next;
        slow.next = list;
        fast.next = head2;
        return new ListNode[] { list, head2 };
    }
}
