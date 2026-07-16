// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

public class ListNode { public int val; public ListNode next; public ListNode(int x) { val = x; } }
public class Solution {
    public bool HasCycle(ListNode head) {
        var slow = head; var fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next; fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}