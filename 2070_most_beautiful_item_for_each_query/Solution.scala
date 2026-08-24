// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

object Solution {
  def maximumBeauty(items: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val sorted = items.sortBy(_(0))
    var maxB = 0
    sorted.foreach { it =>
      maxB = math.max(maxB, it(1))
      it(1) = maxB
    }
    val ans = Array.ofDim[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      var lo = 0
      var hi = sorted.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid)(0) <= queries(i)) lo = mid + 1
        else hi = mid
      }
      ans(i) = if (lo == 0) 0 else sorted(lo - 1)(1)
      i += 1
    }
    ans
  }
}
