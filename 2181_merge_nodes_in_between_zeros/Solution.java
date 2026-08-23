// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        int sum = 0;
        for (ListNode p = head.next; p != null; p = p.next) {
            if (p.val == 0) {
                cur.next = new ListNode(sum);
                cur = cur.next;
                sum = 0;
            } else sum += p.val;
        }
        return dummy.next;
    }
}
