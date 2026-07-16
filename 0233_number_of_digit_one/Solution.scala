// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

object Solution {
  def countDigitOne(n: Int): Int = {
    var count = 0L
    var factor = 1L
    var value = n.toLong
    while (factor <= value) {
      val lower = value % factor
      val current = (value / factor) % 10
      val higher = value / (factor * 10)
      count += current match {
        case 0 => higher * factor
        case 1 => higher * factor + lower + 1
        case _ => (higher + 1) * factor
      }
      factor *= 10
    }
    count.toInt
  }
}
