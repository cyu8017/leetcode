// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

object Solution {
  def numTrees(n: Int): Int = {
    val dp = Array.fill(n + 1)(0)
    dp(0) = 1
    for (nodes <- 1 to n) {
      for (root <- 1 to nodes) {
        dp(nodes) += dp(root - 1) * dp(nodes - root)
      }
    }
    dp(n)
  }
}
