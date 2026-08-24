// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

object Solution {
  def isPreorder(nodes: List[List[Int]]): Boolean = {
    if (nodes.isEmpty) return true
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    stack += nodes.head.head
    var i = 1
    while (i < nodes.length) {
      val id = nodes(i).head
      val parent = nodes(i)(1)
      while (stack.nonEmpty && stack.last != parent) stack.remove(stack.length - 1)
      if (stack.isEmpty) return false
      stack += id
      i += 1
    }
    true
  }
}
