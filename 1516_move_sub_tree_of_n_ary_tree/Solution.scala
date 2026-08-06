// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

import scala.collection.mutable

class Node(_value: Int = 0) {
  var value: Int = _value
  var children: mutable.ListBuffer[Node] = mutable.ListBuffer.empty
}

object Solution {
  def moveSubTree(root: Node, p: Node, q: Node): Node = {
    val parent = mutable.Map.empty[Node, Node]
    def build(node: Node): Unit = {
      for (child <- node.children) {
        parent(child) = node
        build(child)
      }
    }
    build(root)
    if (parent.get(p).contains(q)) return root

    def isAncestor(a: Node, b: Node): Boolean = {
      var cur = b
      while (parent.contains(cur)) {
        cur = parent(cur)
        if (cur eq a) return true
      }
      false
    }

    val pParent = parent.get(p)
    val qParent = parent.get(q)
    var newRoot = root

    if (isAncestor(p, q)) {
      qParent.get.children -= q
      pParent match {
        case None => newRoot = q
        case Some(pp) =>
          val idx = pp.children.indexWhere(_ eq p)
          pp.children(idx) = q
      }
      q.children += p
    } else {
      pParent match {
        case None => newRoot = q
        case Some(pp) => pp.children -= p
      }
      q.children += p
    }
    newRoot
  }
}
