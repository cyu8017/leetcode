// LeetCode 1474 - Delete N Nodes After M Nodes Of A Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode cur = head;
        while (cur != null) {
            for (int i = 0; i < m - 1 && cur != null; i++) cur = cur.next;
            if (cur == null) break;
            ListNode drop = cur.next;
            for (int i = 0; i < n && drop != null; i++) drop = drop.next;
            cur.next = drop;
            cur = drop;
        }
        return head;
    }
}
