// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

object Solution {
  def countGoodSubstrings(s: String): Int = {
    if (s.length < 3) return 0
    var count = 0
    for (i <- 0 until s.length - 2) {
      val window = s.substring(i, i + 3)
      if (window.toSet.size == 3) count += 1
    }
    count
  }
}
