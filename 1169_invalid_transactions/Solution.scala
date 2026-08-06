// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

object Solution {
  def invalidTransactions(transactions: Array[String]): List[String] = {
    val parsed = transactions.map { t =>
      val p = t.split(",")
      (p(0), p(1).toInt, p(2).toInt, p(3), t)
    }
    val invalid = scala.collection.mutable.Set.empty[String]
    for (i <- parsed.indices) {
      val (name, time, amount, city, raw) = parsed(i)
      if (amount > 1000) invalid += raw
      for (j <- parsed.indices if i != j) {
        val (name2, time2, _, city2, raw2) = parsed(j)
        if (name == name2 && city != city2 && math.abs(time - time2) <= 60) {
          invalid += raw
          invalid += raw2
        }
      }
    }
    invalid.toList
  }
}
