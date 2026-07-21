// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

object Solution {
  def maxHappyGroups(batchSize: Int, groups: Array[Int]): Int = {
    val count = Array.fill(batchSize)(0)
    for (size <- groups) count(size % batchSize) += 1
    val memo = scala.collection.mutable.Map.empty[String, Int]

    def dfs(remainder: Int, state: Array[Int]): Int = {
      val key = remainder + "|" + state.mkString(",")
      if (memo.contains(key)) return memo(key)
      var best = 0
      var mod = 1
      while (mod < batchSize) {
        if (state(mod) > 0) {
          state(mod) -= 1
          best = math.max(best, dfs((remainder + mod) % batchSize, state))
          state(mod) += 1
        }
        mod += 1
      }
      if (remainder == 0) best += 1
      memo(key) = best
      best
    }

    var ans = dfs(0, count.clone())
    if (count(0) > 0) ans += count(0) - 1
    ans
  }
}
