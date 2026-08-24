// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

object Solution {
  def solveQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
    val n = nums.length
    val pos = scala.collection.mutable.Map.empty[Int, java.util.ArrayList[Integer]]
    var i = 0
    while (i < n) {
      pos.getOrElseUpdate(nums(i), new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val idx = queries(qi)
      val x = nums(idx)
      val arr = pos(x)
      if (arr.size() == 1) ans(qi) = -1
      else {
        var best = n
        val it = arr.iterator()
        while (it.hasNext) {
          val p = it.next().intValue()
          if (p != idx) {
            var d = math.abs(p - idx)
            d = math.min(d, n - d)
            if (d < best) best = d
          }
        }
        ans(qi) = best
      }
      qi += 1
    }
    ans
  }
}
