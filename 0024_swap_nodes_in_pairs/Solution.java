// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode previous = dummy;

        while (previous.next != null && previous.next.next != null) {
            ListNode first = previous.next;
            ListNode second = previous.next.next;
            first.next = second.next;
            second.next = first;
            previous.next = second;
            previous = first;
        }

        return dummy.next;
    }
}
