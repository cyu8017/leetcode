// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode(var _x: Int = 0) {
  var next: ListNode = null
  var x: Int = _x
}

object Solution {
  def deleteDuplicates(head: ListNode): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var previous = dummy
    var current = head

    while (current != null) {
      if (current.next != null && current.x == current.next.x) {
        while (current.next != null && current.x == current.next.x) {
          current = current.next
        }
        previous.next = current.next
      } else {
        previous = previous.next
      }
      current = current.next
    }

    dummy.next
  }
}
