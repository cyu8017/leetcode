// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

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
    public ListNode DeleteDuplicatesUnsorted(ListNode head) {
        var counts = new Dictionary<int, int>();
        for (var node = head; node != null; node = node.next) {
            counts.TryGetValue(node.val, out int c);
            counts[node.val] = c + 1;
        }

        var dummy = new ListNode(0, head);
        var prev = dummy;
        var cur = head;
        while (cur != null) {
            if (counts[cur.val] > 1) {
                prev.next = cur.next;
                cur = cur.next;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
