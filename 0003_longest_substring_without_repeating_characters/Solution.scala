// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

object Solution {
  def lengthOfLongestSubstring(s: String): Int = {
    val last = scala.collection.mutable.Map.empty[Char, Int]
    var best = 0
    var start = 0

    s.indices.foreach { i =>
      val ch = s(i)
      if (last.contains(ch) && last(ch) >= start) {
        start = last(ch) + 1
      }
      last(ch) = i
      best = math.max(best, i - start + 1)
    }

    best
  }
}
