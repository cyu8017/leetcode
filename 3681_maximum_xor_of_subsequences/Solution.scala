// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

object Solution {
  def maxXorSubsequences(nums: Array[Int]): Int = {
    val basis = new Array[Int](32)
    for (x <- nums) {
      var cur = x
      var b = 31
      var placed = false
      while (b >= 0 && !placed) {
        if ((cur & (1 << b)) != 0) {
          if (basis(b) == 0) {
            basis(b) = cur
            placed = true
          } else cur ^= basis(b)
        }
        if (!placed) b -= 1
      }
    }
    var ans = 0
    var b = 31
    while (b >= 0) {
      if ((ans ^ basis(b)) > ans) ans ^= basis(b)
      b -= 1
    }
    ans
  }
}
