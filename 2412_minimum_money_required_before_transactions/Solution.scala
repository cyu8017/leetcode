// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

object Solution {
  def minimumMoney(transactions: Array[Array[Int]]): Long = {
    var totalLoss = 0L
    var maxCashback = 0L
    var maxCost = 0L
    transactions.foreach { t =>
      val cost = t(0).toLong
      val cashback = t(1).toLong
      if (cost > cashback) {
        totalLoss += cost - cashback
        maxCashback = math.max(maxCashback, cashback)
      } else maxCost = math.max(maxCost, cost)
    }
    math.max(totalLoss + maxCashback, totalLoss + maxCost)
  }
}
