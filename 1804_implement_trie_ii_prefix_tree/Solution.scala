// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

import scala.collection.mutable

class Trie() {
  private class TrieNode {
    val children = mutable.Map.empty[Char, TrieNode]
    var wordCount = 0
    var prefixCount = 0
  }

  private val root = new TrieNode

  def insert(word: String): Unit = {
    var node = root
    for (ch <- word) {
      node = node.children.getOrElseUpdate(ch, new TrieNode)
      node.prefixCount += 1
    }
    node.wordCount += 1
  }

  def countWordsEqualTo(word: String): Int = {
    val node = find(word)
    if (node == null) 0 else node.wordCount
  }

  def countWordsStartingWith(prefix: String): Int = {
    val node = find(prefix)
    if (node == null) 0 else node.prefixCount
  }

  def erase(word: String): Unit = {
    var node = root
    for (ch <- word) {
      node = node.children(ch)
      node.prefixCount -= 1
    }
    node.wordCount -= 1
  }

  private def find(text: String): TrieNode = {
    var node = root
    for (ch <- text) {
      node = node.children.getOrElse(ch, null)
      if (node == null) return null
    }
    node
  }
}
