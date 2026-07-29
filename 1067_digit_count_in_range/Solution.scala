// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

object Solution {
  def digitsCount(d: Int, low: Int, high: Int): Int = {
    def countUpto(n: Int): Int = {
      if (n < 0) return 0
      val s = n.toString
      val length = s.length
      var ans = 0
      for (i <- 0 until length) {
        val left = if (i == 0) 0 else s.substring(0, i).toInt
        val right = if (i + 1 < length) s.substring(i + 1).toInt else 0
        val digit = s(i) - '0'
        val power = math.pow(10, length - i - 1).toInt
        if (d != 0) {
          ans += left * power
          if (digit > d) ans += power
          else if (digit == d) ans += right + 1
        } else if (i != 0) {
          ans += (left - 1) * power
          if (digit > 0) ans += power
          else ans += right + 1
        }
      }
      ans
    }
    countUpto(high) - countUpto(low - 1)
  }
}
