// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

object Solution {
  def movesToMakeZigzag(nums: Array[Int]): Int = {
    def cost(start: Int): Int = {
      var ans = 0
      var i = start
      while (i < nums.length) {
        val left = if (i > 0) nums(i - 1) else Int.MaxValue
        val right = if (i + 1 < nums.length) nums(i + 1) else Int.MaxValue
        ans += math.max(0, nums(i) - math.min(left, right) + 1)
        i += 2
      }
      ans
    }
    math.min(cost(0), cost(1))
  }
}
