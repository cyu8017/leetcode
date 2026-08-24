// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

object Solution {
  def areNumbersAscending(s: String): Boolean = {
    var prev = -1
    s.split(" ").foreach { tok =>
      if (tok.nonEmpty && tok.charAt(0) >= '0' && tok.charAt(0) <= '9') {
        val v = tok.toInt
        if (v <= prev) return false
        prev = v
      }
    }
    true
  }
}
