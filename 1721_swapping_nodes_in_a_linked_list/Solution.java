// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode first = head;
        for (int i = 0; i < k - 1; i++) {
            first = first.next;
        }
        ListNode fast = first;
        ListNode second = head;
        while (fast.next != null) {
            fast = fast.next;
            second = second.next;
        }
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
        return head;
    }
}
