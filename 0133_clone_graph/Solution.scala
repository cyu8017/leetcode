// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

import scala.collection.mutable

object Solution {
  def cloneGraph(node: Node): Node = {
    val clones = mutable.HashMap[Node, Node]()
    def cloneNode(current: Node): Node = {
      if (current == null) return null
      clones.get(current) match {
        case Some(copy) => copy
        case None =>
          val copy = new Node(current.value)
          clones(current) = copy
          copy.neighbors = current.neighbors.map(cloneNode)
          copy
      }
    }
    cloneNode(node)
  }
}
