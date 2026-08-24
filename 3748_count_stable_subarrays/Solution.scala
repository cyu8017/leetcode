// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

object Solution {
  def countStableSubarrays(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val seg = new java.util.ArrayList[Integer]()
    val s = new java.util.ArrayList[java.lang.Long]()
    s.add(0L)
    var l = 0
    var r = 0
    while (r < n) {
      if (r == n - 1 || nums(r) > nums(r + 1)) {
        seg.add(l)
        val k = (r - l + 1).toLong
        s.add(s.get(s.size() - 1) + k * (k + 1) / 2)
        l = r + 1
      }
      r += 1
    }
    val ans = new Array[Long](queries.length)
    var idx = 0
    while (idx < queries.length) {
      val left = queries(idx)(0)
      val right = queries(idx)(1)
      val i = lowerBound(seg, left + 1)
      val j = lowerBound(seg, right + 1) - 1
      if (i > j) {
        val k = (right - left + 1).toLong
        ans(idx) = k * (k + 1) / 2
      } else {
        val a = seg.get(i).toLong - left
        val b = right.toLong - seg.get(j) + 1
        ans(idx) = a * (a + 1) / 2 + s.get(j) - s.get(i) + b * (b + 1) / 2
      }
      idx += 1
    }
    ans
  }

  private def lowerBound(a: java.util.List[Integer], x: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
