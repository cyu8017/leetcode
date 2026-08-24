// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

object Solution {
  def alternatingSubarray(nums: Array[Int]): Int = {
    var ans = -1
    val n = nums.length
    var i = 0
    while (i < n) {
      var j = i + 1
      var ok = true
      while (j < n && ok) {
        val expect = if ((j - i) % 2 == 0) -1 else 1
        if (nums(j) - nums(j - 1) != expect || nums(i + 1) - nums(i) != 1) ok = false
        else {
          ans = math.max(ans, j - i + 1)
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
