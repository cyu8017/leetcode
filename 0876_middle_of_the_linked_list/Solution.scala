// LeetCode 0876 - Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def middleNode(head: ListNode): ListNode = {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
    }
    slow
  }
}
