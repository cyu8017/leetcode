// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

object Solution {
  def cycleLengthQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      var a = queries(i)(0)
      var b = queries(i)(1)
      var steps = 0
      while (a != b) {
        if (a > b) a /= 2 else b /= 2
        steps += 1
      }
      ans(i) = steps + 1
      i += 1
    }
    ans
  }
}
