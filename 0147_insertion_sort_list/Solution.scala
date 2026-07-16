// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

class ListNode(var x: Int = 0) { var next: ListNode = null }
object Solution {
  def insertionSortList(head: ListNode): ListNode = {
    val dummy = new ListNode()
    var current = head
    while (current != null) {
      var previous = dummy
      while (previous.next != null && previous.next.x < current.x) previous = previous.next
      val next = current.next
      current.next = previous.next
      previous.next = current
      current = next
    }
    dummy.next
  }
}