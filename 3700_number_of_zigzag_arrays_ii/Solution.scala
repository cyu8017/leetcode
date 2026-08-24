// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val MOD = 1000000007
    val m = r - l + 1
    if (n == 1) return m % MOD
    var up = Array.fill(m)(1)
    var down = Array.fill(m)(1)
    var length = 2
    while (length <= n) {
      val pref = new Array[Int](m + 1)
      var j = 0
      while (j < m) {
        pref(j + 1) = (pref(j) + down(j)) % MOD
        j += 1
      }
      val nup = new Array[Int](m)
      j = 0
      while (j < m) {
        nup(j) = pref(j)
        j += 1
      }
      val suf = new Array[Int](m + 1)
      j = m - 1
      while (j >= 0) {
        suf(j) = (suf(j + 1) + up(j)) % MOD
        j -= 1
      }
      val ndown = new Array[Int](m)
      j = 0
      while (j < m) {
        ndown(j) = suf(j + 1)
        j += 1
      }
      up = nup
      down = ndown
      length += 1
    }
    var ans = 0
    var j = 0
    while (j < m) {
      ans = (ans + up(j)) % MOD
      ans = (ans + down(j)) % MOD
      j += 1
    }
    ans
  }
}
