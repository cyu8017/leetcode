// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

object Solution {
  def incremovableSubarrayCount(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n) {
        var prev = -1
        var ok = true
        var t = 0
        while (t < n && ok) {
          if (t < i || t > j) {
            if (nums(t) <= prev) ok = false
            else prev = nums(t)
          }
          t += 1
        }
        if (ok) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
