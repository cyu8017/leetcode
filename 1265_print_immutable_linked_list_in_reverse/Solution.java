// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

interface ImmutableListNode {
    void printValue();
    ImmutableListNode getNext();
}

class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        if (head == null) return;
        printLinkedListInReverse(head.getNext());
        head.printValue();
    }
}
