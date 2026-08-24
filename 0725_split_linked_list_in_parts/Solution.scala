// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode(var x: Int = 0) { var next: ListNode = null }

object Solution {
  def splitListToParts(head: ListNode, k: Int): Array[ListNode] = {
    var length = 0
    var node = head
    while (node != null) {
      length += 1
      node = node.next
    }
    val partSize = length / k
    val extra = length % k
    val result = Array.fill[ListNode](k)(null)
    var current = head
    var i = 0
    while (i < k) {
      result(i) = current
      val size = partSize + (if (i < extra) 1 else 0)
      var j = 0
      while (j < size - 1 && current != null) {
        current = current.next
        j += 1
      }
      if (current != null) {
        val nxt = current.next
        current.next = null
        current = nxt
      }
      i += 1
    }
    result
  }
}
