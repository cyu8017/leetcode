// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

object Solution {
  def countSpecialNumbers(n: Int): Int = {
    val s = n.toString
    val m = s.length
    var ans = 0
    var perm = 9
    var i = 1
    while (i < m) {
      ans += perm
      perm *= (10 - i)
      i += 1
    }
    val used = Array.fill(10)(false)
    i = 0
    while (i < m) {
      val start = if (i == 0) 1 else 0
      val digit = s.charAt(i) - '0'
      var d = start
      while (d < digit) {
        if (!used(d)) {
          var rem = 10 - (i + 1)
          var ways = 1
          var j = i + 1
          while (j < m) {
            ways *= rem
            rem -= 1
            j += 1
          }
          ans += ways
        }
        d += 1
      }
      if (used(digit)) return ans
      used(digit) = true
      i += 1
    }
    ans + 1
  }
}
