// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

import scala.collection.mutable

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def postorder(root: Node): List[Int] = {
    val result = mutable.ArrayBuffer.empty[Int]
    dfs(root, result)
    result.toList
  }

  private def dfs(node: Node, result: mutable.ArrayBuffer[Int]): Unit = {
    if (node == null) return
    if (node.children != null) node.children.foreach(child => dfs(child, result))
    result += node.value
  }
}
