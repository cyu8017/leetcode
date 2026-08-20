// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

trait ImmutableListNode {
  def printValue(): Unit
  def getNext(): ImmutableListNode
}

object Solution {
  def printLinkedListInReverse(head: ImmutableListNode): Unit = {
    if (head == null) return
    printLinkedListInReverse(head.getNext())
    head.printValue()
  }
}
