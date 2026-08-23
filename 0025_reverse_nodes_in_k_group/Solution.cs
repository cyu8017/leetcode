// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode ReverseKGroup(ListNode head, int k) {
        var dummy = new ListNode(0, head);
        var groupPrevious = dummy;

        while (true) {
            var kth = groupPrevious;
            for (int i = 0; i < k; i++) {
                kth = kth.next;
                if (kth == null) {
                    return dummy.next;
                }
            }

            var groupNext = kth.next;
            ListNode previous = groupNext;
            var current = groupPrevious.next;

            while (current != groupNext) {
                var next = current.next;
                current.next = previous;
                previous = current;
                current = next;
            }

            var tmp = groupPrevious.next;
            groupPrevious.next = kth;
            groupPrevious = tmp;
        }
    }
}
