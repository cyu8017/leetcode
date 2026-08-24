// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

object Solution {
  def checkGoodInteger(n: Int): Boolean = {
    var x = n
    var s = 0
    while (x > 0) {
      val d = x % 10
      s += d * (d - 1)
      x /= 10
    }
    s >= 50
  }
}
