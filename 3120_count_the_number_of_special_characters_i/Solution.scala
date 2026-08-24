// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

object Solution {
  def numberOfSpecialChars(word: String): Int = {
    val s = new Array[Boolean](128)
    var i = 0
    while (i < word.length) {
      s(word.charAt(i)) = true
      i += 1
    }
    var ans = 0
    i = 0
    while (i < 26) {
      if (s('a' + i) && s('A' + i)) ans += 1
      i += 1
    }
    ans
  }
}
