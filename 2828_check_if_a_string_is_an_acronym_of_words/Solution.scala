// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

object Solution {
  def isAcronym(words: List[String], s: String): Boolean = {
    if (words.length != s.length) return false
    var i = 0
    while (i < words.length) {
      val w = words(i)
      if (w.isEmpty || w.charAt(0) != s.charAt(i)) return false
      i += 1
    }
    true
  }
}
