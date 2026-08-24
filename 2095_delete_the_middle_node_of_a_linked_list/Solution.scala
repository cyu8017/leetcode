// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def deleteMiddle(head: ListNode): ListNode = {
    if (head.next == null) return null
    var slow = head
    var fast = head
    var prev: ListNode = null
    while (fast != null && fast.next != null) {
      prev = slow
      slow = slow.next
      fast = fast.next.next
    }
    prev.next = slow.next
    head
  }
}
