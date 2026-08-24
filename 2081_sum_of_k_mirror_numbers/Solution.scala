// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

object Solution {
  def kMirror(k: Int, n: Int): Long = {
    def isPalBase(x0: Long, bas: Int): Boolean = {
      val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
      var x = x0
      while (x > 0) { digits += (x % bas).toInt; x /= bas }
      var l = 0
      var r = digits.length - 1
      while (l < r) {
        if (digits(l) != digits(r)) return false
        l += 1
        r -= 1
      }
      true
    }
    var ans = 0L
    var count = 0
    var length = 1
    while (count < n) {
      var start = 1
      var i = 1
      while (i < (length + 1) / 2) { start *= 10; i += 1 }
      val end = start * 10
      var half = start
      while (half < end && count < n) {
        var pal = half.toLong
        if (length % 2 == 0) {
          var x = half
          while (x > 0) { pal = pal * 10 + x % 10; x /= 10 }
        } else {
          var x = half / 10
          while (x > 0) { pal = pal * 10 + x % 10; x /= 10 }
        }
        if (isPalBase(pal, k)) { ans += pal; count += 1 }
        half += 1
      }
      length += 1
    }
    ans
  }
}
