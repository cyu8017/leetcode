// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

object Solution {
  def prefixConnected(words: Array[String], k: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[String, Int]
    words.foreach { w =>
      if (w.length >= k) {
        val p = w.substring(0, k)
        cnt(p) = cnt.getOrElse(p, 0) + 1
      }
    }
    var ans = 0
    cnt.values.foreach { v => if (v > 1) ans += 1 }
    ans
  }
}
