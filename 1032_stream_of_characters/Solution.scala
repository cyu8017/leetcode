// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

import scala.collection.mutable

class StreamChecker(_words: Array[String]) {
  private class TrieNode {
    val children = mutable.Map.empty[Char, TrieNode]
    var isWord = false
  }

  private val root = new TrieNode
  private val stream = mutable.ArrayBuffer.empty[Char]

  for (word <- _words) {
    var node = root
    for (ch <- word.reverse) {
      node = node.children.getOrElseUpdate(ch, new TrieNode)
    }
    node.isWord = true
  }

  def query(letter: Char): Boolean = {
    stream += letter
    var node = root
    for (ch <- stream.reverseIterator) {
      if (node.isWord) return true
      node.children.get(ch) match {
        case Some(next) => node = next
        case None => return false
      }
    }
    node.isWord
  }
}
