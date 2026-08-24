// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

object Solution {
  def minCost(nums: Array[Int], costs: Array[Int]): Long = {
    val n = nums.length
    val dp = Array.fill(n)(Long.MaxValue / 4)
    dp(0) = 0L
    val stack1 = scala.collection.mutable.ArrayBuffer.empty[Int]
    val stack2 = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack1.nonEmpty && nums(stack1.last) <= nums(i)) {
        val j = stack1.last
        stack1.remove(stack1.length - 1)
        dp(i) = math.min(dp(i), dp(j) + costs(i))
      }
      while (stack2.nonEmpty && nums(stack2.last) > nums(i)) {
        val j = stack2.last
        stack2.remove(stack2.length - 1)
        dp(i) = math.min(dp(i), dp(j) + costs(i))
      }
      if (stack1.nonEmpty) dp(i) = math.min(dp(i), dp(stack1.last) + costs(i))
      if (stack2.nonEmpty) dp(i) = math.min(dp(i), dp(stack2.last) + costs(i))
      stack1 += i
      stack2 += i
      i += 1
    }
    dp(n - 1)
  }
}
