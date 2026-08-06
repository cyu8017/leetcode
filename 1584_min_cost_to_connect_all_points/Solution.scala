// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

object Solution {
  def minCostConnectPoints(points: Array[Array[Int]]): Int = {
    val n = points.length
    val used = Array.fill(n)(false)
    val dist = Array.fill(n)(Int.MaxValue)
    dist(0) = 0
    var answer = 0
    for (_ <- 0 until n) {
      var u = -1
      for (i <- 0 until n if !used(i) && (u < 0 || dist(i) < dist(u))) u = i
      used(u) = true
      answer += dist(u)
      for (v <- 0 until n if !used(v)) {
        val d = math.abs(points(u)(0) - points(v)(0)) + math.abs(points(u)(1) - points(v)(1))
        dist(v) = math.min(dist(v), d)
      }
    }
    answer
  }
}
