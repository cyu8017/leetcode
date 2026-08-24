// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

object Solution {
  def specialPerm(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val n = nums.length
    val memo = Array.fill(1 << n, n)(-1)
    def dfs(mask: Int, last: Int): Int = {
      if (mask == (1 << n) - 1) return 1
      if (memo(mask)(last) != -1) return memo(mask)(last)
      var res = 0
      var i = 0
      while (i < n) {
        if ((mask & (1 << i)) == 0) {
          if (nums(i) % nums(last) == 0 || nums(last) % nums(i) == 0) {
            res = (res + dfs(mask | (1 << i), i)) % MOD
          }
        }
        i += 1
      }
      memo(mask)(last) = res
      res
    }
    var ans = 0
    var i = 0
    while (i < n) {
      ans = (ans + dfs(1 << i, i)) % MOD
      i += 1
    }
    ans
  }
}
