// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

object Solution {
  def decodeAtIndex(s: String, k: Int): String = {
    var size = 0L
    s.foreach { ch =>
      if (ch.isDigit) size *= (ch - '0')
      else size += 1
    }
    var kk = k.toLong
    var i = s.length - 1
    while (i >= 0) {
      val ch = s.charAt(i)
      kk %= size
      if (kk == 0 && ch.isLetter) return ch.toString
      if (ch.isDigit) size /= (ch - '0')
      else size -= 1
      i -= 1
    }
    ""
  }
}
