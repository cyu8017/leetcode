// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

object Solution {
  def wonderfulSubstrings(word: String): Long = {
    val count = Array.fill(1024)(0L)
    count(0) = 1
    var mask = 0
    var ans = 0L
    for (ch <- word) {
      mask ^= 1 << (ch - 'a')
      ans += count(mask)
      for (bit <- 0 until 10) ans += count(mask ^ (1 << bit))
      count(mask) += 1
    }
    ans
  }
}
