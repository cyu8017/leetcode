// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

object Solution {
  private class Node {
    val children = scala.collection.mutable.HashMap[Int, Node]()
    var cnt = 0
  }

  def countPrefixSuffixPairs(words: Array[String]): Long = {
    val trie = new Node
    var ans = 0L
    for (s <- words) {
      var node = trie
      val m = s.length
      var i = 0
      while (i < m) {
        val p = s.charAt(i) * 32 + s.charAt(m - i - 1)
        node = node.children.getOrElseUpdate(p, new Node)
        ans += node.cnt
        i += 1
      }
      node.cnt += 1
    }
    ans
  }
}
