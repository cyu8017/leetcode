// LeetCode 0086 - Partition List
// https://leetcode.com/problems/partition-list/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
  var x: Int = _x
}

object Solution {
  def partition(head: ListNode, x: Int): ListNode = {
    val beforeHead = new ListNode(0)
    val afterHead = new ListNode(0)
    var before = beforeHead
    var after = afterHead
    var current = head

    while (current != null) {
      if (current.x < x) {
        before.next = current
        before = before.next
      } else {
        after.next = current
        after = after.next
      }
      current = current.next
    }

    after.next = null
    before.next = afterHead.next
    beforeHead.next
  }
}
