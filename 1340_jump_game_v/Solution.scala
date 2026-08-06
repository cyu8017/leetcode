// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

object Solution {
  def maxJumps(arr: Array[Int], d: Int): Int = {
    val n = arr.length
    val dp = Array.fill(n)(1)
    val order = arr.indices.sortBy(arr)
    for (i <- order) {
      for (step <- Array(-1, 1)) {
        var j = i + step
        while (j >= 0 && j < n && math.abs(j - i) <= d && arr(j) < arr(i)) {
          dp(i) = math.max(dp(i), 1 + dp(j))
          j += step
        }
      }
    }
    dp.max
  }
}
