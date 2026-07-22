// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode MergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode pre = list1;
        for (int i = 0; i < a - 1; i++) pre = pre.next;
        ListNode post = pre;
        for (int i = 0; i < b - a + 2; i++) post = post.next;
        pre.next = list2;
        while (pre.next != null) pre = pre.next;
        pre.next = post;
        return list1;
    }
}
