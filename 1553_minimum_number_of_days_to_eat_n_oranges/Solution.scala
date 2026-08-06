// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

object Solution {
  def minDays(n: Int): Int = {
    val memo = scala.collection.mutable.Map.empty[Int, Int]
    def dp(x: Int): Int = {
      if (x <= 1) return x
      memo.getOrElseUpdate(x, 1 + math.min(x % 2 + dp(x / 2), x % 3 + dp(x / 3)))
    }
    dp(n)
  }
}
