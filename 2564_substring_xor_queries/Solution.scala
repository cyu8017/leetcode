// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

object Solution {
  def substringXorQueries(s: String, queries: Array[Array[Int]]): Array[Array[Int]] = {
    val pos = scala.collection.mutable.Map.empty[Int, Array[Int]]
    val n = s.length
    var i = 0
    while (i < n) {
      if (s.charAt(i) == '0') {
        if (!pos.contains(0)) pos(0) = Array(i, i)
      } else {
        var value = 0
        var j = i
        while (j < n && j < i + 30) {
          value = value * 2 + (s.charAt(j) - '0')
          if (!pos.contains(value)) pos(value) = Array(i, j)
          j += 1
        }
      }
      i += 1
    }
    val ans = Array.ofDim[Int](queries.length, 2)
    i = 0
    while (i < queries.length) {
      val need = queries(i)(0) ^ queries(i)(1)
      ans(i) = pos.getOrElse(need, Array(-1, -1)).clone()
      i += 1
    }
    ans
  }
}
