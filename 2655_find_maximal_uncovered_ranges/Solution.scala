// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

object Solution {
  def findMaximalUncoveredRanges(n: Int, ranges: Array[Array[Int]]): Array[Array[Int]] = {
    val sorted = ranges.sortBy(_(0))
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var cur = 0
    var i = 0
    while (i < sorted.length) {
      val r = sorted(i)
      if (r(0) > cur) ans += Array(cur, r(0) - 1)
      if (r(1) + 1 > cur) cur = r(1) + 1
      i += 1
    }
    if (cur < n) ans += Array(cur, n - 1)
    ans.toArray
  }
}
