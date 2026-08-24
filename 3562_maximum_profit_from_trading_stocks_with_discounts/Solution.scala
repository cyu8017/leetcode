// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

object Solution {
  def maxProfit(n: Int, present: Array[Int], future: Array[Int], hierarchy: Array[Array[Int]], budget: Int): Int = {
    val g = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    for (e <- hierarchy) g(e(0)).add(e(1))

    def dfs(u: Int): Array[Array[Int]] = {
      val nxt = Array.ofDim[Int](budget + 1, 2)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        val fv = dfs(v)
        var j = budget
        while (j >= 0) {
          var jv = 0
          while (jv <= j) {
            var pre = 0
            while (pre < 2) {
              nxt(j)(pre) = math.max(nxt(j)(pre), nxt(j - jv)(pre) + fv(jv)(pre))
              pre += 1
            }
            jv += 1
          }
          j -= 1
        }
      }
      val f = Array.ofDim[Int](budget + 1, 2)
      val price = future(u - 1)
      var j = 0
      while (j <= budget) {
        var pre = 0
        while (pre < 2) {
          val cost = present(u - 1) / (pre + 1)
          if (j >= cost) {
            val buyProfit = nxt(j - cost)(1) + (price - cost)
            f(j)(pre) = math.max(nxt(j)(0), buyProfit)
          } else {
            f(j)(pre) = nxt(j)(0)
          }
          pre += 1
        }
        j += 1
      }
      f
    }

    dfs(1)(budget)(0)
  }
}
