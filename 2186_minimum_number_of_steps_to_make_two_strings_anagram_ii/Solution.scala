// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

object Solution {
  def minSteps(s: String, t: String): Int = {
    val freq = Array.fill(26)(0)
    var i = 0
    while (i < s.length) {
      freq(s.charAt(i) - 'a') += 1
      i += 1
    }
    i = 0
    while (i < t.length) {
      freq(t.charAt(i) - 'a') -= 1
      i += 1
    }
    freq.map(math.abs).sum
  }
}
