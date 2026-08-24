// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

object Solution {
  def simulationResult(windows: Array[Int], queries: Array[Int]): Array[Int] = {
    val n = windows.length
    val s = new Array[Boolean](n + 1)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = queries.length - 1
    while (i >= 0) {
      val q = queries(i)
      if (!s(q)) {
        s(q) = true
        ans += q
      }
      i -= 1
    }
    for (w <- windows) if (!s(w)) ans += w
    ans.toArray
  }
}
