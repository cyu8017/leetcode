// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

class ListNode(var x: Int = 0) { var next: ListNode = null }
object Solution {
  def sortList(head: ListNode): ListNode = {
    if (head == null || head.next == null) return head
    var slow = head
    var fast = head
    var previous: ListNode = null
    while (fast != null && fast.next != null) { previous = slow; slow = slow.next; fast = fast.next.next }
    previous.next = null
    merge(sortList(head), sortList(slow))
  }
  private def merge(left: ListNode, right: ListNode): ListNode = {
    val dummy = new ListNode()
    var tail = dummy
    var first = left
    var second = right
    while (first != null && second != null) {
      if (first.x <= second.x) { tail.next = first; first = first.next }
      else { tail.next = second; second = second.next }
      tail = tail.next
    }
    tail.next = if (first != null) first else second
    dummy.next
  }
}