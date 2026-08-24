// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

object Solution {
  def countPrefixes(words: Array[String], s: String): Int = {
    var ans = 0
    for (w <- words) {
      if (w.length <= s.length && s.startsWith(w)) ans += 1
    }
    ans
  }
}
