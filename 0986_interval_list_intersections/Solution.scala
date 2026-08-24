// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

object Solution {
  def intervalIntersection(firstList: Array[Array[Int]], secondList: Array[Array[Int]]): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    var j = 0
    while (i < firstList.length && j < secondList.length) {
      val lo = math.max(firstList(i)(0), secondList(j)(0))
      val hi = math.min(firstList(i)(1), secondList(j)(1))
      if (lo <= hi) ans += Array(lo, hi)
      if (firstList(i)(1) < secondList(j)(1)) i += 1
      else j += 1
    }
    ans.toArray
  }
}
