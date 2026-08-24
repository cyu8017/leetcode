// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

object Solution {
  def longestBalanced(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val vis = new java.util.HashSet[Integer]()
      val cnt = Array(0, 0)
      var j = i
      while (j < n) {
        if (!vis.contains(nums(j))) {
          vis.add(nums(j))
          cnt(nums(j) & 1) += 1
        }
        if (cnt(0) == cnt(1)) ans = math.max(ans, j - i + 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
