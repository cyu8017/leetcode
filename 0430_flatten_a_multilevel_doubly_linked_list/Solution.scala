// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node(
  _value: Int = 0,
  _prev: Node = null,
  _next: Node = null,
  _child: Node = null,
) {
  var value: Int = _value
  var prev: Node = _prev
  var next: Node = _next
  var child: Node = _child
}

object Solution {
  def flatten(head: Node): Node = {
    var current = head
    while (current != null) {
      if (current.child != null) {
        val nextNode = current.next
        val childHead = flatten(current.child)
        current.next = childHead
        childHead.prev = current
        var tail = childHead
        while (tail.next != null) {
          tail = tail.next
        }
        tail.next = nextNode
        if (nextNode != null) {
          nextNode.prev = tail
        }
        current.child = null
      }
      current = current.next
    }
    head
  }
}
