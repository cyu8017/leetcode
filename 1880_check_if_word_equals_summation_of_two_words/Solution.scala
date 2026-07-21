// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

object Solution {
  def isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean = {
    def value(word: String): Int =
      word.map(ch => (ch - 'a').toString).mkString.toInt

    value(firstWord) + value(secondWord) == value(targetWord)
  }
}
