// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

object Solution {
  def numDupDigitsAtMostN(n: Int): Int = {
    val digits = n.toString.map(_ - '0').toArray
    val m = digits.length
    def p(a: Int, b: Int): Int = {
      var res = 1
      for (i <- 0 until b) res *= a - i
      res
    }
    var totalUnique = 0
    for (length <- 1 until m) totalUnique += 9 * p(9, length - 1)
    val used = scala.collection.mutable.Set.empty[Int]
    var broken = false
    for (i <- digits.indices if !broken) {
      val d = digits(i)
      val start = if (i == 0) 1 else 0
      for (x <- start until d if !used.contains(x)) {
        totalUnique += p(9 - i, m - i - 1)
      }
      if (used.contains(d)) broken = true
      else used.add(d)
    }
    if (!broken) totalUnique += 1
    n - totalUnique
  }
}
