// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

object Solution {
  def smallestPalindrome(s: String): String = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    val t = new StringBuilder
    var ch: Char = 0
    var c = 'a'
    while (c <= 'z') {
      val v = cnt(c - 'a') / 2
      var i = 0
      while (i < v) { t.append(c); i += 1 }
      cnt(c - 'a') -= v * 2
      if (cnt(c - 'a') == 1) ch = c
      c = (c + 1).toChar
    }
    val sb = new StringBuilder(t.toString)
    if (ch != 0) sb.append(ch)
    var i = t.length - 1
    while (i >= 0) { sb.append(t.charAt(i)); i -= 1 }
    sb.toString
  }
}
