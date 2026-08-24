// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

object Solution {
  private def fee(x: Int): Int = {
    if (x == 1) 1
    else if (x > 5) 3 * x
    else 2 * x
  }

  def lateFee(daysLate: Array[Int]): Int = {
    var ans = 0
    for (x <- daysLate) ans += fee(x)
    ans
  }
}
