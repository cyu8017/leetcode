// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

object Solution {
  def isCircularSentence(sentence: String): Boolean = {
    val n = sentence.length
    if (sentence.charAt(0) != sentence.charAt(n - 1)) return false
    var i = 0
    while (i < n) {
      if (sentence.charAt(i) == ' ' && sentence.charAt(i - 1) != sentence.charAt(i + 1)) return false
      i += 1
    }
    true
  }
}
