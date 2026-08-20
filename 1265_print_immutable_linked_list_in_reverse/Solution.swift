// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

protocol ImmutableListNode {
    func printValue()
    func getNext() -> ImmutableListNode?
}

class Solution {
    func printLinkedListInReverse(_ head: ImmutableListNode?) {
        guard let head = head else { return }
        printLinkedListInReverse(head.getNext())
        head.printValue()
    }
}
