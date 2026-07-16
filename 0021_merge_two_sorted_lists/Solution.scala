// LeetCode 0021 - Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
    val dummy = new ListNode()
    var current = dummy
    var node1 = list1
    var node2 = list2

    while (node1 != null && node2 != null) {
      if (node1.x <= node2.x) {
        current.next = node1
        node1 = node1.next
      } else {
        current.next = node2
        node2 = node2.next
      }
      current = current.next
    }

    current.next = if (node1 != null) node1 else node2
    dummy.next
  }
}
