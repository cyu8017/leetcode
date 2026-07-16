// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

object Solution {
  def characterReplacement(s: String, k: Int): Int = {
    val counts = Array.fill(26)(0)
    var left = 0
    var best = 0
    var maxCount = 0

    for (right <- s.indices) {
      val index = s(right) - 'A'
      counts(index) += 1
      maxCount = math.max(maxCount, counts(index))
      while ((right - left + 1) - maxCount > k) {
        val leftIndex = s(left) - 'A'
        counts(leftIndex) -= 1
        left += 1
      }
      best = math.max(best, right - left + 1)
    }

    best
  }
}
