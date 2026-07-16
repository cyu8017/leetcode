// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

public class ListNode { public int val; public ListNode next; public ListNode(int x) { val = x; } }
public class Solution {
    public ListNode DetectCycle(ListNode head) {
        var slow = head; var fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next; fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) { slow = slow.next; fast = fast.next; }
                return slow;
            }
        }
        return null;
    }
}