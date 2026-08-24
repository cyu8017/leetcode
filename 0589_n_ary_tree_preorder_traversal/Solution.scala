// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

import scala.collection.mutable

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def preorder(root: Node): List[Int] = {
    val result = mutable.ArrayBuffer.empty[Int]
    dfs(root, result)
    result.toList
  }

  private def dfs(node: Node, result: mutable.ArrayBuffer[Int]): Unit = {
    if (node == null) return
    result += node.value
    if (node.children != null) node.children.foreach(child => dfs(child, result))
  }
}
