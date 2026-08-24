// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

object Solution {
  private val MOD = 1000000007

  private def group(p: Array[Int]): Int = {
    if (p(1) == 0) 0
    else if (p(0) > 0) 1
    else 2
  }

  def maxValue(nums1: Array[Int], nums0: Array[Int]): Int = {
    val n = nums1.length
    val pairs = Array.ofDim[Int](n, 2)
    var b = 0
    var i = 0
    while (i < n) {
      pairs(i)(0) = nums1(i)
      pairs(i)(1) = nums0(i)
      b += nums1(i) + nums0(i)
      i += 1
    }
    java.util.Arrays.sort(pairs, new java.util.Comparator[Array[Int]] {
      def compare(a: Array[Int], c: Array[Int]): Int = {
        val g1 = group(a)
        val g2 = group(c)
        if (g1 != g2) Integer.compare(g1, g2)
        else if (g1 == 0) Integer.compare(c(0), a(0))
        else if (g1 == 1) {
          if (a(0) != c(0)) Integer.compare(c(0), a(0))
          else Integer.compare(a(1), c(1))
        } else Integer.compare(a(1), c(1))
      }
    })
    val p = new Array[Int](b)
    p(0) = 1
    i = 1
    while (i < b) {
      p(i) = ((2L * p(i - 1)) % MOD).toInt
      i += 1
    }
    var ans = 0
    b -= 1
    pairs.foreach { pr =>
      var cnt1 = pr(0)
      var cnt0 = pr(1)
      while (cnt1 > 0) {
        ans = (ans + p(b)) % MOD
        b -= 1
        cnt1 -= 1
      }
      b -= cnt0
    }
    ans
  }
}
