// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        var heap = new PriorityQueue<ListNode, (int val, int order)>();
        int order = 0;

        foreach (var node in lists) {
            if (node != null) {
                heap.Enqueue(node, (node.val, order++));
            }
        }

        var dummy = new ListNode();
        var current = dummy;

        while (heap.Count > 0) {
            var node = heap.Dequeue();
            current.next = node;
            current = current.next;
            if (node.next != null) {
                heap.Enqueue(node.next, (node.next.val, order++));
            }
        }

        return dummy.next;
    }
}
