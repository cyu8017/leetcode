// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

object Solution {
  def maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int = {
    val counts = scala.collection.mutable.Map.empty[String, Int].withDefaultValue(0)
    for (i <- 0 to s.length - minSize) {
      val sub = s.substring(i, i + minSize)
      if (sub.toSet.size <= maxLetters) counts(sub) += 1
    }
    if (counts.isEmpty) 0 else counts.values.max
  }
}
