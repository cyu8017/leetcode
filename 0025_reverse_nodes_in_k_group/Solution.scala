// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def reverseKGroup(head: ListNode, k: Int): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var groupPrevious = dummy

    while (true) {
      var kth = groupPrevious
      var i = 0
      while (i < k) {
        kth = kth.next
        if (kth == null) {
          return dummy.next
        }
        i += 1
      }

      val groupNext = kth.next
      var previous = groupNext
      var current = groupPrevious.next

      while (current ne groupNext) {
        val next = current.next
        current.next = previous
        previous = current
        current = next
      }

      val tmp = groupPrevious.next
      groupPrevious.next = kth
      groupPrevious = tmp
    }
  }
}
