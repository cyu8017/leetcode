// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

object Solution {
  def findNumberOfLIS(nums: Array[Int]): Int = {
    val n = nums.length
    val lengths = Array.fill(n)(1)
    val counts = Array.fill(n)(1)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < i) {
        if (nums(j) < nums(i)) {
          if (lengths(j) + 1 > lengths(i)) {
            lengths(i) = lengths(j) + 1
            counts(i) = counts(j)
          } else if (lengths(j) + 1 == lengths(i)) {
            counts(i) += counts(j)
          }
        }
        j += 1
      }
      i += 1
    }
    var longest = 0
    lengths.foreach(length => longest = math.max(longest, length))
    var answer = 0
    i = 0
    while (i < n) {
      if (lengths(i) == longest) answer += counts(i)
      i += 1
    }
    answer
  }
}
