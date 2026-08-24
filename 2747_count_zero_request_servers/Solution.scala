// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

object Solution {
  def countServers(n: Int, logs: Array[Array[Int]], x: Int, queries: Array[Int]): Array[Int] = {
    java.util.Arrays.sort(logs, (a: Array[Int], b: Array[Int]) => Integer.compare(a(1), b(1)))
    val qs = Array.tabulate(queries.length)(i => Array(queries(i), i))
    java.util.Arrays.sort(qs, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val ans = Array.ofDim[Int](queries.length)
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var active = 0
    var l = 0
    var r = 0
    qs.foreach { q =>
      val t = q(0)
      val qi = q(1)
      while (r < logs.length && logs(r)(1) <= t) {
        val id = logs(r)(0)
        val c = cnt.getOrElse(id, 0)
        if (c == 0) active += 1
        cnt(id) = c + 1
        r += 1
      }
      while (l < r && logs(l)(1) < t - x) {
        val id = logs(l)(0)
        val c = cnt(id) - 1
        cnt(id) = c
        if (c == 0) active -= 1
        l += 1
      }
      ans(qi) = n - active
    }
    ans
  }
}
