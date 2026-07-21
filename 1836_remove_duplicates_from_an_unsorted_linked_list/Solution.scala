// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def deleteDuplicatesUnsorted(head: ListNode): ListNode = {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    var node = head
    while (node != null) {
      counts(node.x) = counts.getOrElse(node.x, 0) + 1
      node = node.next
    }
    val dummy = new ListNode(0, head)
    var prev = dummy
    node = head
    while (node != null) {
      if (counts(node.x) > 1) {
        prev.next = node.next
        node = node.next
      } else {
        prev = node
        node = node.next
      }
    }
    dummy.next
  }
}
