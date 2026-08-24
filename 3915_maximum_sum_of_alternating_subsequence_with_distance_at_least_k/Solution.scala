// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

object Solution {
  private class Fenwick(n: Int) {
    val f = new Array[Long](n)

    def update(i0: Int, value: Long): Unit = {
      var i = i0
      while (i < f.length) {
        f(i) = math.max(f(i), value)
        i += i & -i
      }
    }

    def preMax(i0: Int): Long = {
      var res = 0L
      var i = i0
      while (i > 0) {
        res = math.max(res, f(i))
        i &= i - 1
      }
      res
    }
  }

  def maxAlternatingSum(nums: Array[Int], k: Int): Long = {
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    var m = 0
    var i = 0
    while (i < sorted.length) {
      if (i == 0 || sorted(i) != sorted(i - 1)) {
        sorted(m) = sorted(i)
        m += 1
      }
      i += 1
    }
    val uniq = java.util.Arrays.copyOf(sorted, m)
    val n = nums.length
    val fInc = new Array[Long](n)
    val fDec = new Array[Long](n)
    val inc = new Fenwick(m + 1)
    val dec = new Fenwick(m + 1)
    var ans = 0L
    val ranks = new Array[Int](n)
    i = 0
    while (i < n) {
      val x = nums(i)
      if (i >= k) {
        val j = ranks(i - k)
        inc.update(m - j, fInc(i - k))
        dec.update(j + 1, fDec(i - k))
      }
      var jr = java.util.Arrays.binarySearch(uniq, x)
      if (jr < 0) jr = ~jr
      ranks(i) = jr
      fInc(i) = dec.preMax(jr) + x
      fDec(i) = inc.preMax(m - 1 - jr) + x
      ans = math.max(ans, math.max(fInc(i), fDec(i)))
      i += 1
    }
    ans
  }
}
