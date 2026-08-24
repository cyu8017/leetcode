// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

object Solution {
  def maxNumberOfAlloys(
      n: Int,
      k: Int,
      budget: Int,
      composition: Array[Array[Int]],
      stock: Array[Int],
      cost: Array[Int]
  ): Int = {
    var lo = 0L
    var hi = 1000000000L
    var ans = 0L
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, n, budget, composition, stock, cost)) {
        ans = mid
        lo = mid + 1
      } else hi = mid - 1
    }
    ans.toInt
  }

  private def ok(
      machines: Long,
      n: Int,
      budget: Int,
      composition: Array[Array[Int]],
      stock: Array[Int],
      cost: Array[Int]
  ): Boolean = {
    composition.exists { comp =>
      var spend = 0L
      for (i <- 0 until n) {
        val need = machines * comp(i) - stock(i)
        if (need > 0) spend += need * cost(i)
      }
      spend <= budget
    }
  }
}
