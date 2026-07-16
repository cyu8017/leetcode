// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

object Solution {
  def lengthOfLastWord(s: String): Int = {
    var length = 0
    var i = s.length - 1

    while (i >= 0 && s(i) == ' ') {
      i -= 1
    }

    while (i >= 0 && s(i) != ' ') {
      length += 1
      i -= 1
    }

    length
  }
}
