// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

import scala.collection.mutable

object Solution {
  def wordSquares(words: Array[String]): List[List[String]] = {
    val sortedWords = words.sorted
    val length = sortedWords.head.length
    val prefixMap = mutable.Map("" -> mutable.ListBuffer.from(sortedWords))
    for (word <- sortedWords) {
      for (index <- word.indices) {
        val prefix = word.substring(0, index + 1)
        prefixMap.getOrElseUpdate(prefix, mutable.ListBuffer.empty) += word
      }
    }

    val squares = mutable.ListBuffer[List[String]]()
    val current = mutable.ListBuffer[String]()

    def dfs(row: Int): Unit = {
      if (row == length) {
        squares += current.toList
        return
      }
      val prefix = current.map(_(row)).mkString
      for (candidate <- prefixMap.getOrElse(prefix, Nil)) {
        current += candidate
        dfs(row + 1)
        current.remove(current.length - 1)
      }
    }

    dfs(0)
    squares.toList
  }
}
