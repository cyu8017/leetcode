// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

import scala.collection.mutable.ArrayBuffer

object Solution {
  def maxDepthBST(order: Array[Int]): Int = {
    val nodes = ArrayBuffer.empty[(Int, Int)] // (value, depth)
    var ans = 0
    for (value <- order) {
      var i = 0
      while (i < nodes.length && nodes(i)._1 < value) i += 1
      var depth = 1
      if (i > 0) depth = math.max(depth, nodes(i - 1)._2 + 1)
      if (i < nodes.length) depth = math.max(depth, nodes(i)._2 + 1)
      nodes.insert(i, (value, depth))
      ans = math.max(ans, depth)
    }
    ans
  }
}
