// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

object Solution {
  def findPermutation(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val memo = Array.fill(1 << n, n)(-1)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]

    def absv(x: Int): Int = if (x < 0) -x else x

    def dfs(mask: Int, pre: Int): Int = {
      if (mask == (1 << n) - 1) return absv(pre - nums(0))
      if (memo(mask)(pre) != -1) return memo(mask)(pre)
      var res = Int.MaxValue
      var cur = 1
      while (cur < n) {
        if (((mask >> cur) & 1) == 0) {
          res = math.min(res, absv(pre - nums(cur)) + dfs(mask | (1 << cur), cur))
        }
        cur += 1
      }
      memo(mask)(pre) = res
      res
    }

    def g(mask: Int, pre: Int): Unit = {
      ans += pre
      if (mask == (1 << n) - 1) return
      val res = dfs(mask, pre)
      var cur = 1
      var found = false
      while (cur < n && !found) {
        if (((mask >> cur) & 1) == 0) {
          if (absv(pre - nums(cur)) + dfs(mask | (1 << cur), cur) == res) {
            g(mask | (1 << cur), cur)
            found = true
          }
        }
        cur += 1
      }
    }

    g(1, 0)
    ans.toArray
  }
}
