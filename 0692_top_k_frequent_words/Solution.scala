// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

object Solution {
  def topKFrequent(words: Array[String], k: Int): List[String] = {
    val counts = scala.collection.mutable.HashMap.empty[String, Int]
    for (word <- words) counts(word) = counts.getOrElse(word, 0) + 1
    val ordered = counts.keys.toList.sortWith { (a, b) =>
      val ca = counts(a)
      val cb = counts(b)
      if (ca != cb) ca > cb else a < b
    }
    ordered.take(k)
  }
}
