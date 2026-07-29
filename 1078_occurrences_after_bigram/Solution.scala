// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

object Solution {
  def findOcurrences(text: String, first: String, second: String): Array[String] = {
    val words = text.split(" ")
    (0 until words.length - 2)
      .filter(i => words(i) == first && words(i + 1) == second)
      .map(i => words(i + 2))
      .toArray
  }
}
