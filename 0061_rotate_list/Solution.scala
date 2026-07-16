// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
  var x: Int = _x
}

object Solution {
  def rotateRight(head: ListNode, k: Int): ListNode = {
    if (head == null || head.next == null) {
      return head
    }

    var tail = head
    var length = 1
    while (tail.next != null) {
      tail = tail.next
      length += 1
    }

    tail.next = head
    var remaining = k % length
    if (remaining == 0) {
      tail.next = null
      return head
    }

    val steps = length - remaining
    var newTail = head
    var i = 0
    while (i < steps - 1) {
      newTail = newTail.next
      i += 1
    }

    val newHead = newTail.next
    newTail.next = null
    newHead
  }
}
