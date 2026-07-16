// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

import scala.collection.mutable

object Solution {
  def copyRandomList(head: Node): Node = {
    val clones = mutable.HashMap[Node, Node]()
    def copy(node: Node): Node = {
      if (node == null) return null
      clones.get(node) match {
        case Some(clone) => clone
        case None =>
          val clone = new Node(node.x)
          clones(node) = clone
          clone.next = copy(node.next)
          clone.random = copy(node.random)
          clone
      }
    }
    copy(head)
  }
}
