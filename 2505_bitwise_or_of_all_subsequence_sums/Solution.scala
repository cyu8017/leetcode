// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

object Solution {
  def subsequenceSumOr(nums: Array[Int]): Long = {
    var ans = 0L
    var prefix = 0L
    var i = 0
    while (i < nums.length) {
      prefix += nums(i)
      ans |= nums(i).toLong | prefix
      i += 1
    }
    ans
  }
}
