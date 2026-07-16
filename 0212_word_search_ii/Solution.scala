// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

import scala.collection.mutable

class Solution {
  private class TrieNode {
    val children = mutable.Map[Char, TrieNode]()
    var word: String = _
  }

  private var board: Array[Array[Char]] = _
  private var rows = 0
  private var cols = 0
  private val result = mutable.LinkedHashSet[String]()

  def findWords(board: Array[Array[Char]], words: Array[String]): List[String] = {
    this.board = board
    rows = board.length
    cols = board(0).length

    val root = new TrieNode
    for (word <- words) {
      var node = root
      for (char <- word) node = node.children.getOrElseUpdate(char, new TrieNode)
      node.word = word
    }

    for (row <- 0 until rows; col <- 0 until cols) dfs(row, col, root)
    result.toList
  }

  private def dfs(row: Int, col: Int, node: TrieNode): Unit = {
    val char = board(row)(col)
    val next = node.children.getOrElse(char, return)
    if (next.word != null) {
      result.add(next.word)
      next.word = null
    }
    board(row)(col) = '#'
    if (row + 1 < rows && board(row + 1)(col) != '#') dfs(row + 1, col, next)
    if (row - 1 >= 0 && board(row - 1)(col) != '#') dfs(row - 1, col, next)
    if (col + 1 < cols && board(row)(col + 1) != '#') dfs(row, col + 1, next)
    if (col - 1 >= 0 && board(row)(col - 1) != '#') dfs(row, col - 1, next)
    board(row)(col) = char
    if (next.children.isEmpty) node.children.remove(char)
  }
}
