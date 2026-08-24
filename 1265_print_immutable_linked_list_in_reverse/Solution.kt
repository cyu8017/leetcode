// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

interface ImmutableListNode {
    fun printValue()
    fun getNext(): ImmutableListNode?
}

class Solution {
    fun printLinkedListInReverse(head: ImmutableListNode?) {
        if (head == null) return
        printLinkedListInReverse(head.getNext())
        head.printValue()
    }
}
