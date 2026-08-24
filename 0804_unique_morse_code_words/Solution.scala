// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

object Solution {
  def uniqueMorseRepresentations(words: Array[String]): Int = {
    val codes = Array(
      ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
      "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
      "..-", "...-", ".--", "-..-", "-.--", "--.."
    )
    words.map(w => w.map(ch => codes(ch - 'a')).mkString).toSet.size
  }
}
