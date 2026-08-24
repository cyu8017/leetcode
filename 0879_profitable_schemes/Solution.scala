// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

object Solution {
  def profitableSchemes(n: Int, minProfit: Int, group: Array[Int], profit: Array[Int]): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Int](n + 1, minProfit + 1)
    dp(0)(0) = 1
    var i = 0
    while (i < group.length) {
      val members = group(i)
      val p = profit(i)
      var people = n
      while (people >= members) {
        var prof = minProfit
        while (prof >= 0) {
          val np = math.min(minProfit, prof + p)
          dp(people)(np) = (dp(people)(np) + dp(people - members)(prof)) % MOD
          prof -= 1
        }
        people -= 1
      }
      i += 1
    }
    var ans = 0
    var people = 0
    while (people <= n) {
      ans = (ans + dp(people)(minProfit)) % MOD
      people += 1
    }
    ans
  }
}
