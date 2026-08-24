// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val MOD = 1000000007
    val m = r - l + 1
    if (n == 1) return m % MOD
    var up = Array.fill(m)(1)
    var down = Array.fill(m)(1)
    var len_ = 2
    while (len_ <= n) {
      val prefDown = new Array[Int](m + 1)
      var j = 0
      while (j < m) {
        prefDown(j + 1) = (prefDown(j) + down(j)) % MOD
        j += 1
      }
      val nup = new Array[Int](m)
      j = 0
      while (j < m) {
        nup(j) = prefDown(j)
        j += 1
      }
      val sufUp = new Array[Int](m + 1)
      j = m - 1
      while (j >= 0) {
        sufUp(j) = (sufUp(j + 1) + up(j)) % MOD
        j -= 1
      }
      val ndown = new Array[Int](m)
      j = 0
      while (j < m) {
        ndown(j) = sufUp(j + 1)
        j += 1
      }
      up = nup
      down = ndown
      len_ += 1
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
