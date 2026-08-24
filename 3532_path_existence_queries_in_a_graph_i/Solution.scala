// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

object Solution {
  def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Boolean] = {
    val g = new Array[Int](n)
    var cnt = 0
    var i = 1
    while (i < n) {
      if (nums(i) - nums(i - 1) > maxDiff) cnt += 1
      g(i) = cnt
      i += 1
    }
    val ans = new Array[Boolean](queries.length)
    i = 0
    while (i < queries.length) {
      ans(i) = g(queries(i)(0)) == g(queries(i)(1))
      i += 1
    }
    ans
  }
}
