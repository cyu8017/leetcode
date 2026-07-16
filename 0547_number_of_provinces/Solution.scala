// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

object Solution {
  def findCircleNum(isConnected: Array[Array[Int]]): Int = {
    val n = isConnected.length
    val parent = Array.tabulate(n)(identity)

    def find(x: Int): Int = {
      var node = x
      while (parent(node) != node) {
        parent(node) = parent(parent(node))
        node = parent(node)
      }
      node
    }

    def union(a: Int, b: Int): Unit = {
      val rootA = find(a)
      val rootB = find(b)
      if (rootA != rootB) {
        parent(rootB) = rootA
      }
    }

    for (i <- 0 until n; j <- i + 1 until n if isConnected(i)(j) == 1) {
      union(i, j)
    }

    (0 until n).count(i => find(i) == i)
  }
}
