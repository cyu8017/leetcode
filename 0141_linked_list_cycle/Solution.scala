// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

class ListNode(var x: Int = 0) { var next: ListNode = null }
object Solution {
  def hasCycle(head: ListNode): Boolean = {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
      if (slow eq fast) return true
    }
    false
  }
}