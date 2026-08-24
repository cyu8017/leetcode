// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

object Solution {
  def minimumFuelCost(roads: Array[Array[Int]], seats: Int): Long = {
    val n = roads.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    roads.foreach { r =>
      g(r(0)) += r(1)
      g(r(1)) += r(0)
    }
    var ans = 0L

    def dfs(u: Int, p: Int): Int = {
      var people = 1
      g(u).foreach { v =>
        if (v != p) people += dfs(v, u)
      }
      if (u != 0) ans += (people + seats - 1) / seats
      people
    }

    dfs(0, -1)
    ans
  }
}
