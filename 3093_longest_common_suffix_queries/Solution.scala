// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

object Solution {
  private val INF = 1 << 30

  private class Trie {
    val children: Array[Trie] = new Array[Trie](26)
    var length: Int = INF
    var idx: Int = INF
  }

  def stringIndices(wordsContainer: Array[String], wordsQuery: Array[String]): Array[Int] = {
    val trie = new Trie()
    var i = 0
    while (i < wordsContainer.length) {
      insert(trie, wordsContainer(i), i)
      i += 1
    }
    val ans = new Array[Int](wordsQuery.length)
    i = 0
    while (i < wordsQuery.length) {
      ans(i) = query(trie, wordsQuery(i))
      i += 1
    }
    ans
  }

  private def insert(t: Trie, w: String, i: Int): Unit = {
    var node = t
    if (node.length > w.length) {
      node.length = w.length
      node.idx = i
    }
    var k = w.length - 1
    while (k >= 0) {
      val id = w.charAt(k) - 'a'
      if (node.children(id) == null) node.children(id) = new Trie()
      node = node.children(id)
      if (node.length > w.length) {
        node.length = w.length
        node.idx = i
      }
      k -= 1
    }
  }

  private def query(t: Trie, w: String): Int = {
    var node = t
    var k = w.length - 1
    while (k >= 0) {
      val id = w.charAt(k) - 'a'
      if (node.children(id) == null) return node.idx
      node = node.children(id)
      k -= 1
    }
    node.idx
  }
}
