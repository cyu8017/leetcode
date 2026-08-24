// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

object Solution {
  def maxScore(nums: Array[Int]): Int = {
    val n = nums.length
    val f = new Array[Int](n)
    def dfs(i: Int): Int = {
      if (f(i) > 0) return f(i)
      var j = i + 1
      while (j < n) {
        f(i) = math.max(f(i), (j - i) * nums(j) + dfs(j))
        j += 1
      }
      f(i)
    }
    dfs(0)
  }
}
