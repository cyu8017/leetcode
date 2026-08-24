// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

object Solution {
  def calculateTax(brackets: Array[Array[Int]], income: Int): Double = {
    var ans = 0.0
    var prev = 0
    for (b <- brackets) {
      val upper = b(0)
      val percent = b(1)
      if (income <= prev) return ans
      val taxable = if (income < upper) income - prev else upper - prev
      ans += taxable * percent / 100.0
      prev = upper
    }
    ans
  }
}
