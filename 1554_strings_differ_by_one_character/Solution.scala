// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

object Solution {
  def differByOne(dict: Array[String]): Boolean = {
    val seen = scala.collection.mutable.Set.empty[String]
    for (word <- dict; i <- word.indices) {
      val pattern = word.substring(0, i) + "*" + word.substring(i + 1)
      if (seen.contains(pattern)) return true
      seen += pattern
    }
    false
  }
}
