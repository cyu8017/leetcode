// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

object Solution {
  def lenLongestFibSubseq(arr: Array[Int]): Int = {
    val n = arr.length
    val index = arr.zipWithIndex.toMap
    val dp = Array.fill(n, n)(2)
    var ans = 0
    var j = 0
    while (j < n) {
      var i = 0
      while (i < j) {
        index.get(arr(j) - arr(i)) match {
          case Some(k) if k < i =>
            dp(i)(j) = dp(k)(i) + 1
            ans = math.max(ans, dp(i)(j))
          case _ =>
        }
        i += 1
      }
      j += 1
    }
    if (ans >= 3) ans else 0
  }
}
