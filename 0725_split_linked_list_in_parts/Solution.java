// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int length = 0;
        for (ListNode node = head; node != null; node = node.next) length++;
        int partSize = length / k, extra = length % k;
        ListNode[] result = new ListNode[k];
        ListNode current = head;
        for (int i = 0; i < k; i++) {
            result[i] = current;
            int size = partSize + (i < extra ? 1 : 0);
            for (int j = 0; j < size - 1 && current != null; j++) current = current.next;
            if (current != null) {
                ListNode nxt = current.next;
                current.next = null;
                current = nxt;
            }
        }
        return result;
    }
}
