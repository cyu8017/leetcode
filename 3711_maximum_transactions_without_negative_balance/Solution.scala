// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

object Solution {
  def maxTransactions(transactions: Array[Int]): Int = {
    val tm = new java.util.TreeMap[Integer, Integer]()
    var ans = transactions.length
    var s = 0L
    for (x <- transactions) {
      s += x
      tm.merge(x, 1, Integer.sum)
      while (s < 0) {
        val y = tm.firstKey.intValue()
        s -= y
        ans -= 1
        val c = tm.get(y)
        if (c == 1) tm.remove(y)
        else tm.put(y, c - 1)
      }
    }
    ans
  }
}
