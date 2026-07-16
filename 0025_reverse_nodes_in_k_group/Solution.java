// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head);
        ListNode groupPrevious = dummy;

        while (true) {
            ListNode kth = groupPrevious;
            for (int i = 0; i < k; i++) {
                kth = kth.next;
                if (kth == null) {
                    return dummy.next;
                }
            }

            ListNode groupNext = kth.next;
            ListNode previous = groupNext;
            ListNode current = groupPrevious.next;

            while (current != groupNext) {
                ListNode next = current.next;
                current.next = previous;
                previous = current;
                current = next;
            }

            ListNode tmp = groupPrevious.next;
            groupPrevious.next = kth;
            groupPrevious = tmp;
        }
    }
}
