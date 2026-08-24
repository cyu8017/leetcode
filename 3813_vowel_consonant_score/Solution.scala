// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

object Solution {
  def vowelConsonantScore(s: String): Int = {
    var v = 0
    var c = 0
    s.foreach { ch =>
      if (Character.isLetter(ch)) {
        c += 1
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v += 1
      }
    }
    c -= v
    if (c == 0) 0 else v / c
  }
}
