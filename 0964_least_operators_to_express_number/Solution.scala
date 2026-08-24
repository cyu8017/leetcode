// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

object Solution {
  def leastOpsExpressTarget(x: Int, target: Int): Int = {
    val memo = scala.collection.mutable.Map.empty[Int, Int]
    def dfs(t: Int): Int = {
      if (memo.contains(t)) return memo(t)
      if (x > t) {
        val ans = math.min(2 * t - 1, 2 * (x - t))
        memo(t) = ans
        return ans
      }
      if (x == t) {
        memo(t) = 0
        return 0
      }
      var prod = x.toLong
      var n = 0
      while (prod < t) {
        prod *= x
        n += 1
      }
      if (prod == t) {
        memo(t) = n
        return n
      }
      var ans = dfs(t - (prod / x).toInt) + n
      if (prod < 2L * t) ans = math.min(ans, dfs(prod.toInt - t) + n + 1)
      memo(t) = ans
      ans
    }
    dfs(target)
  }
}
