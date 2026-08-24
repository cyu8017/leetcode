// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

object Solution {
  def findWordsContaining(words: Array[String], x: Char): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 0
    while (i < words.length) {
      if (words(i).indexOf(x) >= 0) ans += i
      i += 1
    }
    ans.toList
  }
}
