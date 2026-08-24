// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

object Solution {
  def subarrayMajority(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      val t = queries(qi)(2)
      val cnt = new java.util.HashMap[Integer, Integer]()
      var i = l
      while (i <= r) {
        cnt.merge(nums(i), 1, Integer.sum)
        i += 1
      }
      var best = -1
      var bestC = 0
      val it = cnt.entrySet().iterator()
      while (it.hasNext) {
        val e = it.next()
        val v = e.getKey.intValue()
        val c = e.getValue.intValue()
        if (c >= t && (c > bestC || (c == bestC && (best == -1 || v < best)))) {
          bestC = c
          best = v
        }
      }
      ans(qi) = best
      qi += 1
    }
    ans
  }
}
