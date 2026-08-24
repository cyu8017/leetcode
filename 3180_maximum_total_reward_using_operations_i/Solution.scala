// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

object Solution {
  def maxTotalReward(rewardValues: Array[Int]): Int = {
    java.util.Arrays.sort(rewardValues)
    val n = rewardValues.length
    val f = Array.fill(rewardValues(n - 1) << 1)(-1)
    def upperBound(a: Array[Int], x: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) <= x) lo = mid + 1 else hi = mid
      }
      lo
    }
    def dfs(x: Int): Int = {
      if (f(x) != -1) return f(x)
      val idx = upperBound(rewardValues, x)
      f(x) = 0
      var it = idx
      while (it < n) {
        f(x) = math.max(f(x), rewardValues(it) + dfs(x + rewardValues(it)))
        it += 1
      }
      f(x)
    }
    dfs(0)
  }
}
