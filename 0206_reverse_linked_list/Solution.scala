// LeetCode 0206 - Reverse Linked List\n// https://leetcode.com/problems/\n\nclass ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def reverseList(head: ListNode): ListNode = {
    var current = head
    var previous: ListNode = null
    while (current != null) { val next = current.next; current.next = previous; previous = current; current = next }
    previous
  }
}
