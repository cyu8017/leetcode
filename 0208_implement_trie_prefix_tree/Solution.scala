// LeetCode 0208 - Implement Trie (Prefix Tree)\n// https://leetcode.com/problems/\n\nimport scala.collection.mutable

class Trie {
  private class TrieNode { val children = mutable.Map[Char, TrieNode](); var isWord = false }
  private val root = new TrieNode

  def insert(word: String): Unit = {
    var node = root
    for (char <- word) node = node.children.getOrElseUpdate(char, new TrieNode)
    node.isWord = true
  }

  def search(word: String): Boolean = Option(find(word)).exists(_.isWord)
  def startsWith(prefix: String): Boolean = find(prefix) != null

  private def find(text: String): TrieNode = {
    var node = root
    for (char <- text) {
      node = node.children.getOrElse(char, null)
      if (node == null) return null
    }
    node
  }
}
