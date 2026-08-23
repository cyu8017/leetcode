// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
class Solution {
    public ListNode removeNodes(ListNode head) {
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
        return rev(dummy.next);
    }

    private ListNode rev(ListNode node) {
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
