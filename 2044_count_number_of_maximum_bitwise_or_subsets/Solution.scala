// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

object Solution {
  def countMaxOrSubsets(nums: Array[Int]): Int = {
    var maxOr = 0
    nums.foreach { x => maxOr |= x }
    var ans = 0
    def dfs(i: Int, cur: Int): Unit = {
      if (i == nums.length) { if (cur == maxOr) ans += 1; return }
      dfs(i + 1, cur)
      dfs(i + 1, cur | nums(i))
    }
    dfs(0, 0)
    ans
  }
}
