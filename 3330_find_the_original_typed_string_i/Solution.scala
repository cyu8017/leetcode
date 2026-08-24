// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

object Solution {
  def possibleStringCount(word: String): Int = {
    var ans = 1
    var i = 1
    while (i < word.length) {
      if (word.charAt(i) == word.charAt(i - 1)) ans += 1
      i += 1
    }
    ans
  }
}
