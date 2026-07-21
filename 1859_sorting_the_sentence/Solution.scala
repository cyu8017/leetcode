// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

object Solution {
  def sortSentence(s: String): String = {
    val tokens = s.split(" ")
    val ordered = Array.fill(tokens.length)("")
    for (token <- tokens) {
      val position = token.last.asDigit - 1
      ordered(position) = token.substring(0, token.length - 1)
    }
    ordered.mkString(" ")
  }
}
