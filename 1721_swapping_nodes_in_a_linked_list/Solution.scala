// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def swapNodes(head: ListNode, k: Int): ListNode = {
    var first = head
    for (_ <- 0 until k - 1) {
      first = first.next
    }
    var fast = first
    var second = head
    while (fast.next != null) {
      fast = fast.next
      second = second.next
    }
    val temp = first.x
    first.x = second.x
    second.x = temp
    head
  }
}
