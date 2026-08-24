// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

object Solution {
  def minimumOperations(nums: List[Int]): Int = {
    val n = nums.length
    val INF = 1 << 30
    val dp = Array.fill(n + 1, 4)(INF)
    dp(0)(1) = 0
    dp(0)(2) = 0
    dp(0)(3) = 0
    var i = 1
    while (i <= n) {
      val v = nums(i - 1)
      var g = 1
      while (g <= 3) {
        val cost = if (v != g) 1 else 0
        var prev = 1
        while (prev <= g) {
          dp(i)(g) = math.min(dp(i)(g), dp(i - 1)(prev) + cost)
          prev += 1
        }
        g += 1
      }
      i += 1
    }
    math.min(dp(n)(1), math.min(dp(n)(2), dp(n)(3)))
  }
}
