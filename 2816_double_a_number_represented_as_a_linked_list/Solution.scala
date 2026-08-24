// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def doubleIt(head0: ListNode): ListNode = {
    def rev(node0: ListNode): ListNode = {
      var node = node0
      var prev: ListNode = null
      while (node != null) {
        val nxt = node.next
        node.next = prev
        prev = node
        node = nxt
      }
      prev
    }
    var head = rev(head0)
    var carry = 0
    var cur = head
    var prev: ListNode = null
    while (cur != null) {
      val value = cur.x * 2 + carry
      cur.x = value % 10
      carry = value / 10
      prev = cur
      cur = cur.next
    }
    if (carry > 0) prev.next = new ListNode(carry)
    rev(head)
  }
}
