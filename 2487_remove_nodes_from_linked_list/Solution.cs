// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}
public class Solution {
    public ListNode RemoveNodes(ListNode head) {
        head = Rev(head);
        int mx = 0;
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while (prev.next != null) {
            if (prev.next.val >= mx) {
                mx = prev.next.val;
                prev = prev.next;
            } else {
                prev.next = prev.next.next;
            }
        }
        return Rev(dummy.next);
    }

    private ListNode Rev(ListNode node) {
        ListNode prev = null;
        while (node != null) {
            ListNode nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    }
}
