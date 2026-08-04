// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public int getDecimalValue(ListNode head) {
        int value = 0;
        while (head != null) {
            value = value * 2 + head.val;
            head = head.next;
        }
        return value;
    }
}
