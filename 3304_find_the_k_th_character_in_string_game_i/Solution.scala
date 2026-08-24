// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

object Solution {
  def kthCharacter(k: Int): Char = {
    val s = new StringBuilder("a")
    while (s.length < k) {
      val n = s.length
      var i = 0
      while (i < n) {
        s.append(('a' + ((s.charAt(i) - 'a' + 1) % 26)).toChar)
        i += 1
      }
    }
    s.charAt(k - 1)
  }
}
