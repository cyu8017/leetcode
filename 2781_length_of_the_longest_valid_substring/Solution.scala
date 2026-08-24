// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

object Solution {
  def longestValidSubstring(word: String, forbidden: List[String]): Int = {
    val forbid = forbidden.toSet
    var maxLen = 0
    forbidden.foreach(f => maxLen = math.max(maxLen, f.length))
    var ans = 0
    var right = word.length - 1
    var left = word.length - 1
    while (left >= 0) {
      var k = left
      var stop = false
      while (!stop && k <= right && k - left + 1 <= maxLen) {
        if (forbid.contains(word.substring(left, k + 1))) {
          right = k - 1
          stop = true
        } else k += 1
      }
      ans = math.max(ans, right - left + 1)
      left -= 1
    }
    ans
  }
}
