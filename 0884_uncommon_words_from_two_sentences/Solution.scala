// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

object Solution {
  def uncommonFromSentences(s1: String, s2: String): Array[String] = {
    val count = scala.collection.mutable.Map.empty[String, Int]
    def add(s: String): Unit = {
      s.split(" ").foreach { w =>
        if (w.nonEmpty) count(w) = count.getOrElse(w, 0) + 1
      }
    }
    add(s1)
    add(s2)
    count.collect { case (w, c) if c == 1 => w }.toArray
  }
}
