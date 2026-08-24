// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

object Solution {
  def isGood(nums: Array[Int]): Boolean = {
    val n = nums.length - 1
    if (n < 1) return false
    val freq = Array.ofDim[Int](n + 1)
    nums.foreach { v =>
      if (v < 1 || v > n) return false
      freq(v) += 1
    }
    var i = 1
    while (i < n) {
      if (freq(i) != 1) return false
      i += 1
    }
    freq(n) == 2
  }
}
