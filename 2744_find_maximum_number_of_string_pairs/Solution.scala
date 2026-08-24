// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

object Solution {
  def maximumNumberOfStringPairs(words: Array[String]): Int = {
    val freq = scala.collection.mutable.Map.empty[String, Int]
    var ans = 0
    words.foreach { w =>
      val rev = w.reverse
      val c = freq.getOrElse(rev, 0)
      if (c > 0) {
        ans += 1
        freq(rev) = c - 1
      } else {
        freq(w) = freq.getOrElse(w, 0) + 1
      }
    }
    ans
  }
}
