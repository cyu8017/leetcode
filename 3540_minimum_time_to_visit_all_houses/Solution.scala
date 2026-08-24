// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

object Solution {
  def minTotalTime(forward: Array[Int], backward: Array[Int], queries: Array[Int]): Long = {
    val n = forward.length
    var sumB = 0
    for (v <- backward) sumB += v
    val pf = new Array[Int](n + 1)
    val pb = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pf(i + 1) = pf(i) + forward(i)
      pb(i + 1) = pb(i) + backward(i)
      i += 1
    }
    var ans = 0L
    var pos = 0
    for (q <- queries) {
      var r = 0
      if (q < pos) r = pf(n)
      r += pf(q) - pf(pos)
      var l = 0
      if (q > pos) l = sumB
      l += pb(pos) - pb(q)
      ans += math.min(l, r)
      pos = q
    }
    ans
  }
}
