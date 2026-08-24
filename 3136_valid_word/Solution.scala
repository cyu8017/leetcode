// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

object Solution {
  def isValid(word: String): Boolean = {
    if (word.length < 3) return false
    var hasVowel = false
    var hasConsonant = false
    val vs = new Array[Boolean](26)
    "aeiou".foreach(c => vs(c - 'a') = true)
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (Character.isLetter(c)) {
        val lower = Character.toLowerCase(c)
        if (vs(lower - 'a')) hasVowel = true
        else hasConsonant = true
      } else if (!Character.isDigit(c)) {
        return false
      }
      i += 1
    }
    hasVowel && hasConsonant
  }
}
