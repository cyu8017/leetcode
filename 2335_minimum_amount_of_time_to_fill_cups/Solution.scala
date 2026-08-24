// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

object Solution {
  def fillCups(amount: Array[Int]): Int = {
    var a = amount(0)
    var b = amount(1)
    var c = amount(2)
    if (a < b) { val t = a; a = b; b = t }
    if (a < c) { val t = a; a = c; c = t }
    if (b < c) { val t = b; b = c; c = t }
    if (a >= b + c) a else (a + b + c + 1) / 2
  }
}
