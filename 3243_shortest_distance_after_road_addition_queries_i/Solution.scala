// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

object Solution {
  def shortestDistanceAfterQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < n - 1) { g(i) += i + 1; i += 1 }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      g(queries(i)(0)) += queries(i)(1)
      ans(i) = bfs(g, n, 0)
      i += 1
    }
    ans
  }

  def bfs(g: Array[scala.collection.mutable.ArrayBuffer[Int]], n: Int, start: Int): Int = {
    val q = scala.collection.mutable.Queue[Int]()
    q.enqueue(start)
    val vis = new Array[Boolean](n)
    vis(start) = true
    var d = 0
    while (true) {
      var k = q.size
      while (k > 0) {
        val u = q.dequeue()
        if (u == n - 1) return d
        for (v <- g(u) if !vis(v)) {
          vis(v) = true
          q.enqueue(v)
        }
        k -= 1
      }
      d += 1
    }
    -1
  }
}
