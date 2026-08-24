// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def sortLinkedList(head: ListNode): ListNode = {
    if (head == null) return null
    var h = head
    var prev = head
    var cur = head.next
    while (cur != null) {
      if (cur.x < 0) {
        prev.next = cur.next
        cur.next = h
        h = cur
        cur = prev.next
      } else {
        prev = cur
        cur = cur.next
      }
    }
    h
  }
}
