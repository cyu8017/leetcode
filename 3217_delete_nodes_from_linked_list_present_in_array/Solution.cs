// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

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
    public ListNode ModifiedList(int[] nums, ListNode head) {
        var s = new HashSet<int>(nums);
        var dummy = new ListNode(0, head);
        for (ListNode pre = dummy; pre.next != null; ) {
            if (s.Contains(pre.next.val)) pre.next = pre.next.next;
            else pre = pre.next;
        }
        return dummy.next;
    }
}
