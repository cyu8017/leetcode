// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

object Solution {
  def maxRequests(requests: Array[Array[Int]], k: Int, window: Int): Int = {
    val g = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    requests.foreach { r =>
      g.getOrElseUpdate(r(0), scala.collection.mutable.ArrayBuffer.empty[Int]) += r(1)
    }
    var ans = requests.length
    g.values.foreach { ts =>
      val sorted = ts.sorted
      val kept = scala.collection.mutable.ArrayBuffer.empty[Int]
      sorted.foreach { t =>
        while (kept.nonEmpty && t - kept(0) > window) kept.remove(0)
        if (kept.length < k) kept += t
        else ans -= 1
      }
    }
    ans
  }
}
