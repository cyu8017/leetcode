// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

object Solution {
  def countPairs(nums: List[Int], target: Int): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      var j = i + 1
      while (j < nums.length) {
        if (nums(i) + nums(j) < target) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
