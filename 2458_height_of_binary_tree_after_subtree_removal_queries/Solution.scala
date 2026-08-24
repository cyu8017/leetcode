// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def treeQueries(root: TreeNode, queries: Array[Int]): Array[Int] = {
    val height = scala.collection.mutable.Map.empty[Int, Int]
    val level = scala.collection.mutable.Map.empty[Int, Int]
    val levelMax = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]

    def dfs(node: TreeNode, d: Int): Int = {
      if (node == null) return -1
      level(node.value) = d
      val h = 1 + math.max(dfs(node.left, d + 1), dfs(node.right, d + 1))
      height(node.value) = h
      val arr = levelMax.getOrElseUpdate(d, scala.collection.mutable.ArrayBuffer.empty[Int])
      if (arr.isEmpty) arr += h
      else if (h >= arr(0)) {
        if (arr.length == 1) arr += arr(0)
        else arr(1) = arr(0)
        arr(0) = h
      } else if (arr.length == 1 || h > arr(1)) {
        if (arr.length == 1) arr += h
        else arr(1) = h
      }
      h
    }

    dfs(root, 0)
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val q = queries(i)
      val d = level(q)
      val h = height(q)
      val top = levelMax(d)
      if (top(0) == h) {
        if (top.length > 1) ans(i) = d + top(1)
        else ans(i) = d - 1
      } else {
        ans(i) = d + top(0)
      }
      i += 1
    }
    ans
  }
}
