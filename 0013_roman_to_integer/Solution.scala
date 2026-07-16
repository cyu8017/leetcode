// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

object Solution {
  def romanToInt(s: String): Int = {
    val values = Map(
      'I' -> 1, 'V' -> 5, 'X' -> 10, 'L' -> 50,
      'C' -> 100, 'D' -> 500, 'M' -> 1000,
    )
    var total = 0
    var prev = 0

    s.reverse.foreach { ch =>
      val curr = values(ch)
      if (curr < prev) total -= curr
      else total += curr
      prev = curr
    }

    total
  }
}
