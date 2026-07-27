// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

object Solution {
  def maximalNetworkRank(n: Int, roads: Array[Array[Int]]): Int = {
    val degree = Array.fill(n)(0)
    val edges = scala.collection.mutable.Set.empty[(Int, Int)]
    for (r <- roads) {
      val a = r(0)
      val b = r(1)
      degree(a) += 1
      degree(b) += 1
      edges += ((math.min(a, b), math.max(a, b)))
    }
    var ans = 0
    for (a <- 0 until n; b <- a + 1 until n) {
      val linked = if (edges.contains((a, b))) 1 else 0
      ans = math.max(ans, degree(a) + degree(b) - linked)
    }
    ans
  }
}
