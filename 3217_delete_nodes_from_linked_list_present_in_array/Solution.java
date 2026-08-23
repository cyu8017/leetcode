// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

import java.util.HashSet;
import java.util.Set;

class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        var s = new HashSet<Integer>(nums);
        var dummy = new ListNode(0, head);
        for (ListNode pre = dummy; pre.next != null; ) {
            if (s.contains(pre.next.val)) pre.next = pre.next.next;
            else pre = pre.next;
        }
        return dummy.next;
    }
}
