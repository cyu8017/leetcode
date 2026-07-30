// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode RemoveZeroSumSublists(ListNode head) {
        var dummy = new ListNode(0, head);
        int prefix = 0;
        var seen = new Dictionary<int, ListNode> { [0] = dummy };
        var node = dummy;
        while (node != null) {
            prefix += node.val;
            seen[prefix] = node;
            node = node.next;
        }
        prefix = 0;
        node = dummy;
        while (node != null) {
            prefix += node.val;
            node.next = seen[prefix].next;
            node = node.next;
        }
        return dummy.next;
    }
}
