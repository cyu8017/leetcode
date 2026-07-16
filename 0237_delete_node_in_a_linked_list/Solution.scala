// LeetCode 0237 - Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def deleteNode(node: ListNode): Unit = {
    node.x = node.next.x
    node.next = node.next.next
  }
}
