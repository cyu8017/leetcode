// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], diff: Int): Long = {
    val n = nums1.length
    val arr = Array.tabulate(n)(i => nums1(i) - nums2(i))
    val tmp = new Array[Int](n)

    def mergeCount(l: Int, r: Int): Long = {
      if (r - l <= 1) return 0L
      val m = (l + r) / 2
      var ans = mergeCount(l, m) + mergeCount(m, r)
      var j = m
      var i = l
      while (i < m) {
        while (j < r && arr(j) < arr(i) - diff) j += 1
        ans += r - j
        i += 1
      }
      var p = l
      var q = m
      var i2 = l
      while (p < m && q < r) {
        if (arr(p) <= arr(q)) {
          tmp(i2) = arr(p); p += 1
        } else {
          tmp(i2) = arr(q); q += 1
        }
        i2 += 1
      }
      while (p < m) { tmp(i2) = arr(p); p += 1; i2 += 1 }
      while (q < r) { tmp(i2) = arr(q); q += 1; i2 += 1 }
      var t = l
      while (t < r) { arr(t) = tmp(t); t += 1 }
      ans
    }

    mergeCount(0, n)
  }
}
