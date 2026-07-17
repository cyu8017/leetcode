// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

object Solution {
  def countPairs(n: Int, edges: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val deg = new Array[Int](n + 1)
    val shared = scala.collection.mutable.Map.empty[(Int, Int), Int]
    for (edge <- edges) {
      val a = math.min(edge(0), edge(1))
      val b = math.max(edge(0), edge(1))
      deg(a) += 1
      deg(b) += 1
      shared((a, b)) = shared.getOrElse((a, b), 0) + 1
    }
    val sortedDeg = deg.slice(1, n + 1).sorted
    queries.map { q =>
      var res = 0
      var left = 0
      var right = n - 1
      while (left < right) {
        if (sortedDeg(left) + sortedDeg(right) > q) {
          res += right - left
          right -= 1
        } else {
          left += 1
        }
      }
      for (((a, b), count) <- shared) {
        val sum = deg(a) + deg(b)
        if (sum > q && q >= sum - count) {
          res -= 1
        }
      }
      res
    }
  }
}
