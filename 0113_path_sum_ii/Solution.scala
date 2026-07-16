// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

import scala.collection.mutable.ListBuffer

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
    val paths = ListBuffer[List[Int]]()
    def dfs(node: TreeNode, remaining: Int, path: List[Int]): Unit = {
      if (node != null) {
        val next = path :+ node.value
        if (node.left == null && node.right == null && node.value == remaining)
          paths += next
        else {
          dfs(node.left, remaining - node.value, next)
          dfs(node.right, remaining - node.value, next)
        }
      }
    }
    dfs(root, targetSum, Nil)
    paths.toList
  }
}