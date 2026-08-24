// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

object Solution {
  private val INF = 1 << 29

  def minimumValueSum(nums: Array[Int], andValues: Array[Int]): Int = {
    val n = nums.length
    val m = andValues.length
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Int, j: Int, a0: Int): Int = {
      if (n - i < m - j) return INF
      if (j == m) return if (i == n) 0 else INF
      val a = a0 & nums(i)
      if (a < andValues(j)) return INF
      val key = (i.toLong << 36) | (j.toLong << 32) | (a.toLong & 0xffffffffL)
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = dfs(i + 1, j, a)
          if (a == andValues(j)) ans = math.min(ans, dfs(i + 1, j + 1, -1) + nums(i))
          f(key) = ans
          ans
      }
    }

    val ans = dfs(0, 0, -1)
    if (ans < INF) ans else -1
  }
}
