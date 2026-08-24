// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def modifiedList(nums: Array[Int], head: ListNode): ListNode = {
    val s = scala.collection.mutable.HashSet.from(nums)
    val dummy = new ListNode(0, head)
    var pre = dummy
    while (pre.next != null) {
      if (s.contains(pre.next.x)) pre.next = pre.next.next
      else pre = pre.next
    }
    dummy.next
  }
}
