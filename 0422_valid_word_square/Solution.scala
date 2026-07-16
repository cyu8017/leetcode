// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

object Solution {
  def validWordSquare(words: Array[String]): Boolean = {
    for ((row, word) <- words.zipWithIndex) {
      for ((col, char) <- word.zipWithIndex) {
        if (col >= words.length || row >= words(col).length || words(col)(row) != char) {
          return false
        }
      }
    }
    true
  }
}
