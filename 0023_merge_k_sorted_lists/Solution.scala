// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

import scala.collection.mutable.PriorityQueue

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def mergeKLists(lists: Array[ListNode]): ListNode = {
    implicit val ord: Ordering[(Int, Int, ListNode)] =
      Ordering.by[(Int, Int, ListNode), (Int, Int)](entry => (entry._1, entry._2))

    val heap = PriorityQueue.empty[(Int, Int, ListNode)]
    var order = 0

    lists.foreach { node =>
      if (node != null) {
        heap.enqueue((node.x, order, node))
        order += 1
      }
    }

    val dummy = new ListNode()
    var current = dummy

    while (heap.nonEmpty) {
      val node = heap.dequeue()._3
      current.next = node
      current = current.next
      if (node.next != null) {
        heap.enqueue((node.next.x, order, node.next))
        order += 1
      }
    }

    dummy.next
  }
}
