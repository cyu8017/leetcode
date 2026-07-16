// LeetCode 0117 - Populating Next Right Pointers in Each Node II
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import scala.collection.mutable.Queue

class Node(var value: Int = 0, var left: Node = null, var right: Node = null,
           var next: Node = null)

object Solution {
  def connect(root: Node): Node = {
    if (root == null) return null
    val queue = Queue[Node](root)
    while (queue.nonEmpty) {
      var previous: Node = null
      val size = queue.size
      for (_ <- 0 until size) {
        val node = queue.dequeue()
        if (previous != null) previous.next = node
        previous = node
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
      previous.next = null
    }
    root
  }
}