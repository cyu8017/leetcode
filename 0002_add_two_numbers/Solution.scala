// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val dummy = new ListNode()
    var current = dummy
    var node1 = l1
    var node2 = l2
    var carry = 0

    while (node1 != null || node2 != null || carry != 0) {
      var total = carry
      if (node1 != null) {
        total += node1.x
        node1 = node1.next
      }
      if (node2 != null) {
        total += node2.x
        node2 = node2.next
      }
      carry = total / 10
      current.next = new ListNode(total % 10)
      current = current.next
    }

    dummy.next
  }
}
