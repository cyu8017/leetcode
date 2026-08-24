// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

object Solution {
  def closestFair(n: Int): Int = {
    var x = n
    while (true) {
      val s = x.toString
      if (s.length % 2 != 0) {
        var p = 1
        var i = 0
        while (i < s.length) {
          p *= 10
          i += 1
        }
        return closestFair(p)
      }
      var even = 0
      var odd = 0
      var i = 0
      while (i < s.length) {
        if ((s.charAt(i) - '0') % 2 == 0) even += 1
        else odd += 1
        i += 1
      }
      if (even == odd) return x
      x += 1
    }
    0
  }
}
