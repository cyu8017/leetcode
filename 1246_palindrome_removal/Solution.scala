// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

object Solution {
  def minimumMoves(arr: Array[Int]): Int = {
    val n = arr.length
    val dp = Array.ofDim[Int](n, n)
    for (i <- 0 until n) dp(i)(i) = 1
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      dp(i)(j) = 1 + dp(i + 1)(j)
      if (arr(i) == arr(i + 1)) dp(i)(j) = math.min(dp(i)(j), 1 + (if (i + 2 <= j) dp(i + 2)(j) else 0))
      for (k <- i + 2 to j if arr(i) == arr(k)) {
        dp(i)(j) = math.min(dp(i)(j), dp(i + 1)(k - 1) + (if (k < j) dp(k + 1)(j) else 0))
      }
    }
    dp(0)(n - 1)
  }
}
