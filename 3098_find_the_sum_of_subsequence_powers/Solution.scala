// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

object Solution {
  private val MOD = 1000000007

  def sumOfPowers(nums0: Array[Int], k: Int): Int = {
    val nums = nums0.sorted
    val n = nums.length
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Int, j: Int, kk: Int, mi: Int): Int = {
      if (i >= n) return if (kk == 0) mi else 0
      if (n - i < kk) return 0
      val key = (mi.toLong << 18) | (i.toLong << 12) | (j.toLong << 6) | kk
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = dfs(i + 1, j, kk, mi)
          if (j == n) ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
          else ans = (ans + dfs(i + 1, i, kk - 1, math.min(mi, nums(i) - nums(j)))) % MOD
          f(key) = ans
          ans
      }
    }

    dfs(0, n, k, Int.MaxValue)
  }
}
