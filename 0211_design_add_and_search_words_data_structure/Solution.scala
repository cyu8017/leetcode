// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

import scala.collection.mutable

class WordDictionary {
  private class TrieNode {
    val children = mutable.Map[Char, TrieNode]()
    var isWord = false
  }

  private val root = new TrieNode

  def addWord(word: String): Unit = {
    var node = root
    for (char <- word) node = node.children.getOrElseUpdate(char, new TrieNode)
    node.isWord = true
  }

  def search(word: String): Boolean = dfs(root, word, 0)

  private def dfs(node: TrieNode, word: String, index: Int): Boolean = {
    if (index == word.length) return node.isWord
    val char = word(index)
    if (char == '.') {
      node.children.values.exists(child => dfs(child, word, index + 1))
    } else {
      node.children.get(char) match {
        case Some(next) => dfs(next, word, index + 1)
        case None => false
      }
    }
  }
}
