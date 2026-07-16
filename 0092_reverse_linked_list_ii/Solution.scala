// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
  var x: Int = _x
}

object Solution {
  def reverseBetween(head: ListNode, left: Int, right: Int): ListNode = {
    if (head == null || left == right) {
      return head
    }

    val dummy = new ListNode(0)
    dummy.next = head
    var before = dummy
    var i = 0
    while (i < left - 1) {
      before = before.next
      i += 1
    }

    val start = before.next
    var current = start.next
    i = 0
    while (i < right - left) {
      start.next = current.next
      current.next = before.next
      before.next = current
      current = start.next
      i += 1
    }

    dummy.next
  }
}
