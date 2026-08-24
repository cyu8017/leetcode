// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

object Solution {
  def minimumOperationsToMakeKPeriodic(word: String, k: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[String, Int]
    val n = word.length
    var mx = 0
    var i = 0
    while (i < n) {
      val s = word.substring(i, i + k)
      val v = cnt.getOrElse(s, 0) + 1
      cnt(s) = v
      mx = math.max(mx, v)
      i += k
    }
    n / k - mx
  }
}
