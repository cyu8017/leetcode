// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

object Solution {
  def stoneGameVII(stones: Array[Int]): Int = {
    val n = stones.length
    val pre = Array.fill(n + 1)(0)
    for (i <- stones.indices) pre(i + 1) = pre(i) + stones(i)
    val dp = Array.ofDim[Int](n, n)
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      val left = pre(j + 1) - pre(i + 1) - dp(i + 1)(j)
      val right = pre(j) - pre(i) - dp(i)(j - 1)
      dp(i)(j) = math.max(left, right)
    }
    dp(0)(n - 1)
  }
}
