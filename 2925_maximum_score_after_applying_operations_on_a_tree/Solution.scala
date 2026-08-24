// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var values: Array[Int] = _

  def maximumScoreAfterOperations(edges: Array[Array[Int]], values: Array[Int]): Long = {
    val n = values.length
    this.values = values
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var total = 0L
    values.foreach(v => total += v)
    total - dfs(0, -1)
  }

  private def dfs(u: Int, p: Int): Long = {
    var sumKids = 0L
    var isLeaf = true
    g(u).foreach { v =>
      if (v != p) {
        isLeaf = false
        sumKids += dfs(v, u)
      }
    }
    if (isLeaf) values(u).toLong
    else if (values(u) < sumKids) values(u).toLong else sumKids
  }
}
