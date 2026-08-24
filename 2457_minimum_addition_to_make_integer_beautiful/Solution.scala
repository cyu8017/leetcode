// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

object Solution {
  def makeIntegerBeautiful(n: Long, target: Int): Long = {
    def digitSum(x0: Long): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += (x % 10).toInt
        x /= 10
      }
      s
    }
    val orig = n
    var cur = n
    var pow10 = 1L
    while (digitSum(cur) > target) {
      cur = cur / 10 + 1
      pow10 *= 10
    }
    cur * pow10 - orig
  }
}
