// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def swapPairs(head: ListNode): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var previous = dummy

    while (previous.next != null && previous.next.next != null) {
      val first = previous.next
      val second = first.next
      first.next = second.next
      second.next = first
      previous.next = second
      previous = first
    }

    dummy.next
  }
}
