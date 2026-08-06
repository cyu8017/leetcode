// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def findRoot(tree: Array[Node]): Node = {
    var xor = 0
    val nodes = scala.collection.mutable.Map.empty[Int, Node]
    for (node <- tree) {
      nodes(node.value) = node
      xor ^= node.value
      for (child <- node.children) xor ^= child.value
    }
    nodes(xor)
  }
}
