// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

object Solution {
  def resultsArray(queries: Array[Array[Int]], k: Int): Array[Int] = {
    val h = new java.util.PriorityQueue[Int]((a: Int, b: Int) => Integer.compare(b, a))
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val d = math.abs(queries(i)(0)) + math.abs(queries(i)(1))
      h.offer(d)
      if (h.size > k) h.poll()
      ans(i) = if (h.size < k) -1 else h.peek()
      i += 1
    }
    ans
  }
}
