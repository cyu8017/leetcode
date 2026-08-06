// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeZeroSumSublists(head: ListNode): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var prefix = 0
    val seen = scala.collection.mutable.Map(0 -> dummy)
    var node = dummy
    while (node != null) {
      prefix += node.x
      seen(prefix) = node
      node = node.next
    }
    prefix = 0
    node = dummy
    while (node != null) {
      prefix += node.x
      node.next = seen(prefix).next
      node = node.next
    }
    dummy.next
  }
}
