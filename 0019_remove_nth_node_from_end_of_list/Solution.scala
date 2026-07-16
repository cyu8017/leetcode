// LeetCode 0019 - Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var fast: ListNode = dummy
    var slow: ListNode = dummy

    var i = 0
    while (i < n) {
      fast = fast.next
      i += 1
    }

    while (fast.next != null) {
      fast = fast.next
      slow = slow.next
    }

    slow.next = slow.next.next
    dummy.next
  }
}
