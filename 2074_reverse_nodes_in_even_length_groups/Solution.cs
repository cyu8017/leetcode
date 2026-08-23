// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode ReverseEvenLengthGroups(ListNode head) {
        var dummy = new ListNode(0, head);
        ListNode prev = dummy;
        int group = 1;
        while (prev.next != null) {
            ListNode cur = prev.next;
            int cnt = 0;
            ListNode node = cur;
            while (node != null && cnt < group) { node = node.next; cnt++; }
            if (cnt % 2 == 0) {
                ListNode revPrev = node;
                ListNode p = cur;
                for (int i = 0; i < cnt; i++) {
                    ListNode nxt = p.next;
                    p.next = revPrev;
                    revPrev = p;
                    p = nxt;
                }
                prev.next = revPrev;
                prev = cur;
            } else {
                for (int i = 0; i < cnt; i++) prev = prev.next;
            }
            group++;
        }
        return dummy.next;
    }
}
