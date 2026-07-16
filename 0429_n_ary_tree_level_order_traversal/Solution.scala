// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

import scala.collection.mutable

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def levelOrder(root: Node): List[List[Int]] = {
    if (root == null) {
      return List.empty
    }

    val result = mutable.ListBuffer[List[Int]]()
    val queue = mutable.Queue[Node](root)

    while (queue.nonEmpty) {
      val size = queue.size
      val level = mutable.ListBuffer[Int]()
      for (_ <- 0 until size) {
        val node = queue.dequeue()
        level += node.value
        queue.enqueueAll(node.children)
      }
      result += level.toList
    }

    result.toList
  }
}
