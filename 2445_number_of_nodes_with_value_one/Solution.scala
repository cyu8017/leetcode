// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

object Solution {
  def numberOfNodes(n: Int, queries: Array[Int]): Int = {
    val flip = new Array[Int](n + 1)
    val value = new Array[Int](n + 1)
    var i = 0
    while (i < queries.length) {
      flip(queries(i)) ^= 1
      i += 1
    }
    var ans = 0
    i = 1
    while (i <= n) {
      value(i) = flip(i)
      if (i > 1) value(i) ^= value(i / 2)
      ans += value(i)
      i += 1
    }
    ans
  }
}
