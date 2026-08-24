// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

object Solution {
  def leftmostBuildingQueries(heights: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val qn = queries.length
    val ans = Array.fill(qn)(-1)
    val buckets = Array.fill(heights.length)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    var qi = 0
    while (qi < qn) {
      var a = queries(qi)(0)
      var b = queries(qi)(1)
      if (a > b) { val t = a; a = b; b = t }
      if (a == b || heights(a) < heights(b)) ans(qi) = b
      else buckets(b) += Array(heights(a), qi)
      qi += 1
    }
    val st = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = heights.length - 1
    while (i >= 0) {
      for (p <- buckets(i)) {
        val h = p(0)
        val qii = p(1)
        var lo = 0
        var hi = st.length - 1
        var pos = -1
        while (lo <= hi) {
          val mid = (lo + hi) / 2
          if (st(mid)(0) > h) {
            pos = st(mid)(1)
            lo = mid + 1
          } else hi = mid - 1
        }
        ans(qii) = pos
      }
      while (st.nonEmpty && st.last(0) <= heights(i)) st.remove(st.length - 1)
      st += Array(heights(i), i)
      i -= 1
    }
    ans
  }
}
