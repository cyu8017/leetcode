// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

object Solution {
  def maxValue(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n)
    val preMax = new Array[Int](n)
    preMax(0) = nums(0)
    var i = 1
    while (i < n) {
      preMax(i) = math.max(preMax(i - 1), nums(i))
      i += 1
    }
    var sufMin = Int.MaxValue / 2
    i = n - 1
    while (i >= 0) {
      if (preMax(i) > sufMin) ans(i) = ans(i + 1)
      else ans(i) = preMax(i)
      sufMin = math.min(sufMin, nums(i))
      i -= 1
    }
    ans
  }
}
