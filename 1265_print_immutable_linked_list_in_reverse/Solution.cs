// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

public class ImmutableListNode {
    public virtual void PrintValue() { }
    public virtual ImmutableListNode GetNext() { return null; }
}

public class Solution {
    public void PrintLinkedListInReverse(ImmutableListNode head) {
        if (head == null) return;
        PrintLinkedListInReverse(head.GetNext());
        head.PrintValue();
    }
}
