// LeetCode 3965 - Finish Time of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

import scala.collection.mutable

object Solution {
  private var g: Array[mutable.ArrayBuffer[Int]] = Array.empty
  private var baseTime: Array[Int] = Array.empty

  def finishTime(n: Int, edges: Array[Array[Int]], baseTimeArr: Array[Int]): Long = {
    baseTime = baseTimeArr
    g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    for (e <- edges) g(e(0)) += e(1)
    dfs(0)
  }

  private def dfs(i: Int): Long = {
    if (g(i).isEmpty) return baseTime(i)
    val INF = 1L << 62
    var earliest = INF
    var latest = -INF
    for (j <- g(i)) {
      val a = dfs(j)
      earliest = math.min(earliest, a)
      latest = math.max(latest, a)
    }
    val ownDuration = (latest - earliest) + baseTime(i)
    latest + ownDuration
  }
}
