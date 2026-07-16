// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
  var x: Int = _x
}

object Solution {
  def deleteDuplicates(head: ListNode): ListNode = {
    var current = head

    while (current != null && current.next != null) {
      if (current.x == current.next.x) {
        current.next = current.next.next
      } else {
        current = current.next
      }
    }

    head
  }
}
