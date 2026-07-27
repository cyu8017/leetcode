// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

object Solution {
  def countDistinct(s: String): Int = {
    class TrieNode {
      val children = scala.collection.mutable.Map.empty[Char, TrieNode]
    }
    val root = new TrieNode
    var ans = 0
    for (i <- s.indices) {
      var node = root
      for (j <- i until s.length) {
        val c = s(j)
        if (!node.children.contains(c)) {
          node.children(c) = new TrieNode
          ans += 1
        }
        node = node.children(c)
      }
    }
    ans
  }
}
