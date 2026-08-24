// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

object Solution {
  def waysToReachStair(k: Int): Int = {
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Long, j: Int, jump: Int): Int = {
      if (i > k + 1) return 0
      val key = (i << 32) | (jump.toLong << 1) | j
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = 0
          if (i == k) ans += 1
          if (i > 0 && j == 0) ans += dfs(i - 1, 1, jump)
          ans += dfs(i + (1L << jump), 0, jump + 1)
          f(key) = ans
          ans
      }
    }

    dfs(1, 0, 0)
  }
}
