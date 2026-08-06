// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

object Solution {
  def numKLenSubstrNoRepeats(s: String, k: Int): Int = {
    if (k > s.length) return 0
    val window = scala.collection.mutable.Map.empty[Char, Int]
    for (i <- 0 until k) {
      window(s(i)) = window.getOrElse(s(i), 0) + 1
    }
    var ans = if (window.size == k) 1 else 0
    for (i <- k until s.length) {
      window(s(i)) = window.getOrElse(s(i), 0) + 1
      val left = s(i - k)
      window(left) = window(left) - 1
      if (window(left) == 0) window.remove(left)
      if (window.size == k) ans += 1
    }
    ans
  }
}
