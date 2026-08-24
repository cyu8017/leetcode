// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

object Solution {
  private val MX = 50
  private val C: Array[Array[Long]] = {
    val arr = Array.ofDim[Long](MX, MX + 1)
    var i = 0
    while (i < MX) {
      arr(i)(0) = 1
      var j = 1
      while (j <= i) {
        arr(i)(j) = arr(i - 1)(j - 1) + arr(i - 1)(j)
        j += 1
      }
      i += 1
    }
    arr
  }

  def nthSmallest(n0: Long, k0: Int): Long = {
    var n = n0
    var k = k0
    var ans = 0L
    var i = 49
    while (i >= 0) {
      if (n > C(i)(k)) {
        n -= C(i)(k)
        ans |= 1L << i
        k -= 1
        if (k == 0) return ans
      }
      i -= 1
    }
    ans
  }
}
