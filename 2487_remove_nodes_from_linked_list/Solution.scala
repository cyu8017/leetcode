// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeNodes(head0: ListNode): ListNode = {
    def rev(node0: ListNode): ListNode = {
      var prev: ListNode = null
      var node = node0
      while (node != null) {
        val nxt = node.next
        node.next = prev
        prev = node
        node = nxt
      }
      prev
    }
    var head = rev(head0)
    var mx = 0
    val dummy = new ListNode(0, head)
    var prev = dummy
    while (prev.next != null) {
      if (prev.next.x >= mx) {
        mx = prev.next.x
        prev = prev.next
      } else {
        prev.next = prev.next.next
      }
    }
    rev(dummy.next)
  }
}
