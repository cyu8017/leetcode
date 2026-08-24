// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

object Solution {
  def minElement(nums: Array[Int]): Int = {
    var ans = 1000000000
    for (num <- nums) {
      var x = num
      var s = 0
      while (x > 0) {
        s += x % 10
        x /= 10
      }
      if (s < ans) ans = s
    }
    ans
  }
}
