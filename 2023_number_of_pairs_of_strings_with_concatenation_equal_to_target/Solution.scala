// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

object Solution {
  def numOfPairs(nums: Array[String], target: String): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      var j = 0
      while (j < nums.length) {
        if (i != j && nums(i) + nums(j) == target) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
