// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

object Solution {
  def minInversionCount(nums: Array[Int], k: Int): Long = {
    var vals = nums.clone()
    java.util.Arrays.sort(vals)
    val u = unique(vals)
    vals = java.util.Arrays.copyOf(vals, u)
    val bit = new Array[Int](vals.length + 1)

    def add(i0: Int, delta: Int): Unit = {
      var i = i0
      while (i < bit.length) {
        bit(i) += delta
        i += i & -i
      }
    }

    def sum(i0: Int): Int = {
      var i = i0
      var res = 0
      while (i > 0) {
        res += bit(i)
        i -= i & -i
      }
      res
    }

    val rank = new Array[Int](nums.length)
    var inv = 0L
    var i = 0
    while (i < nums.length) {
      rank(i) = lowerBound(vals, nums(i)) + 1
      if (i < k) {
        inv += i - sum(rank(i))
        add(rank(i), 1)
      }
      i += 1
    }
    var best = inv
    var r = k
    while (r < nums.length) {
      val left = rank(r - k)
      inv -= sum(left - 1)
      add(left, -1)
      inv += k - 1 - sum(rank(r))
      add(rank(r), 1)
      if (inv < best) best = inv
      r += 1
    }
    best
  }

  private def unique(a: Array[Int]): Int = {
    var n = 0
    var i = 0
    while (i < a.length) {
      if (n == 0 || a(i) != a(n - 1)) {
        a(n) = a(i)
        n += 1
      }
      i += 1
    }
    n
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
