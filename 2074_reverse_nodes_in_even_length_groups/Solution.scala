// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def reverseEvenLengthGroups(head: ListNode): ListNode = {
    val dummy = new ListNode(0, head)
    var prev = dummy
    var group = 1
    while (prev.next != null) {
      var cur = prev.next
      var cnt = 0
      var node = cur
      while (node != null && cnt < group) { node = node.next; cnt += 1 }
      if (cnt % 2 == 0) {
        var revPrev = node
        var p = cur
        var i = 0
        while (i < cnt) {
          val nxt = p.next
          p.next = revPrev
          revPrev = p
          p = nxt
          i += 1
        }
        prev.next = revPrev
        prev = cur
      } else {
        var i = 0
        while (i < cnt) { prev = prev.next; i += 1 }
      }
      group += 1
    }
    dummy.next
  }
}
