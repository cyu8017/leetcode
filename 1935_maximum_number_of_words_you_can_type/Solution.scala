// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

object Solution {
  def canBeTypedWords(text: String, brokenLetters: String): Int = {
    val broken = brokenLetters.toSet
    text.split(" ").count(w => !w.exists(broken.contains))
  }
}
