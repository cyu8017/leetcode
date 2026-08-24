// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

object Solution {
  def sumOfGoodNumbers(nums: Array[Int], k: Int): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      val x = nums(i)
      var good = true
      if (i - k >= 0 && x <= nums(i - k)) good = false
      if (i + k < n && x <= nums(i + k)) good = false
      if (good) ans += x
      i += 1
    }
    ans
  }
}
