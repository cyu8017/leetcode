// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def mergeNodes(head: ListNode): ListNode = {
    val dummy = new ListNode()
    var cur = dummy
    var sum = 0
    var p = head.next
    while (p != null) {
      if (p.x == 0) {
        cur.next = new ListNode(sum)
        cur = cur.next
        sum = 0
      } else sum += p.x
      p = p.next
    }
    dummy.next
  }
}
