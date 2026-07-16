// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode(var x: Int = 0) { var next: ListNode = null }
object Solution {
  def detectCycle(head: ListNode): ListNode = {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
      if (slow eq fast) {
        slow = head
        while (!(slow eq fast)) { slow = slow.next; fast = fast.next }
        return slow
      }
    }
    null
  }
}