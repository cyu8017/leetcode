// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode SwapPairs(ListNode head) {
        var dummy = new ListNode(0, head);
        var previous = dummy;

        while (previous.next != null && previous.next.next != null) {
            var first = previous.next;
            var second = previous.next.next;
            first.next = second.next;
            second.next = first;
            previous.next = second;
            previous = first;
        }

        return dummy.next;
    }
}
