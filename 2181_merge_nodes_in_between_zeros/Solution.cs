// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode MergeNodes(ListNode head) {
        var dummy = new ListNode();
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
