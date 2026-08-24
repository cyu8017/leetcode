// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

object Solution {
  def greatestLetter(s: String): String = {
    val lower = Array.fill(26)(false)
    val upper = Array.fill(26)(false)
    s.foreach { c =>
      if (c >= 'a' && c <= 'z') lower(c - 'a') = true
      else upper(c - 'A') = true
    }
    var i = 25
    while (i >= 0) {
      if (lower(i) && upper(i)) return ('A' + i).toChar.toString
      i -= 1
    }
    ""
  }
}
