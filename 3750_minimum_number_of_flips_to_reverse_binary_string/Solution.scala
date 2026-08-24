// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

object Solution {
  def minimumFlips(n: Int): Int = {
    var x = n.toLong
    val s = if (x == 0) "0" else {
      val sb = new StringBuilder
      while (x > 0) {
        sb.append(('0' + (x & 1).toInt).toChar)
        x >>= 1
      }
      val arr = sb.toString.toCharArray
      reverse(arr, 0, arr.length)
      new String(arr)
    }
    val m = s.length
    var cnt = 0
    var i = 0
    while (i < m / 2) {
      if (s.charAt(i) != s.charAt(m - i - 1)) cnt += 1
      i += 1
    }
    cnt * 2
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
