// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode pre = list1;
        for (int i = 0; i < a - 1; i++) {
            pre = pre.next;
        }
        ListNode post = pre;
        for (int i = 0; i < b - a + 2; i++) {
            post = post.next;
        }
        pre.next = list2;
        while (pre.next != null) {
            pre = pre.next;
        }
        pre.next = post;
        return list1;
    }
}
