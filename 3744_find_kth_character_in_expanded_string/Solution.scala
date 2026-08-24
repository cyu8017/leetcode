// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

object Solution {
  def kthCharacter(s: String, k0: Long): Char = {
    var k = k0
    val words = s.trim.split("\\s+")
    words.foreach { w =>
      val m = (1L + w.length) * w.length / 2
      if (k == m) return ' '
      if (k > m) {
        k -= m + 1
      } else {
        var cur = 0L
        var i = 0
        while (true) {
          cur += i + 1
          if (k < cur) return w.charAt(i)
          i += 1
        }
      }
    }
    ' '
  }
}
