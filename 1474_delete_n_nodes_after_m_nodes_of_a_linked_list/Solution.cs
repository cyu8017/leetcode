// LeetCode 1474 - Delete N Nodes After M Nodes Of A Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

public class ListNode {
    public int val; public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}
public class Solution {
    public ListNode DeleteNodes(ListNode head, int m, int n) {
        var cur = head;
        while (cur != null) {
            for (int i = 0; i < m - 1 && cur != null; i++) cur = cur.next;
            if (cur == null) break;
            var drop = cur.next;
            for (int i = 0; i < n && drop != null; i++) drop = drop.next;
            cur.next = drop; cur = drop;
        }
        return head;
    }
}
