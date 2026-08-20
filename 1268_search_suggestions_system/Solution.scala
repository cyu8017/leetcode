// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

object Solution {
  def suggestedProducts(products: Array[String], searchWord: String): List[List[String]] = {
    val sorted = products.sorted
    val answer = scala.collection.mutable.ListBuffer.empty[List[String]]
    var prefix = ""
    for (ch <- searchWord) {
      prefix += ch
      var lo = 0
      var hi = sorted.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid) < prefix) lo = mid + 1 else hi = mid
      }
      answer += sorted.slice(lo, lo + 3).filter(_.startsWith(prefix)).toList
    }
    answer.toList
  }
}
