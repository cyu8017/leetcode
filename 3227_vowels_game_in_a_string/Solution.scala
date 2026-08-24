// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

object Solution {
  def doesAliceWin(s: String): Boolean = {
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true
      i += 1
    }
    false
  }
}
