// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

object Solution {
  def minimumDiameterAfterMerge(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Int = {
    val d1 = treeDiameter(edges1)
    val d2 = treeDiameter(edges2)
    math.max(math.max(d1, d2), (d1 + 1) / 2 + (d2 + 1) / 2 + 1)
  }

  def treeDiameter(edges: Array[Array[Int]]): Int = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0
    var a = 0
    def dfs(i: Int, fa: Int, t: Int): Unit = {
      for (j <- g(i)) if (j != fa) dfs(j, i, t + 1)
      if (ans < t) { ans = t; a = i }
    }
    dfs(0, -1, 0)
    dfs(a, -1, 0)
    ans
  }
}
