// LeetCode 0203 - Remove Linked List Elements\n// https://leetcode.com/problems/\n\nclass ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeElements(head: ListNode, `val`: Int): ListNode = {
    val dummy = new ListNode(0, head)
    var current = dummy
    while (current.next != null) {
      if (current.next.x == `val`) current.next = current.next.next
      else current = current.next
    }
    dummy.next
  }
}
