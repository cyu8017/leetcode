// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

object Solution {
  def findSubstringInWraproundString(s: String): Int = {
    val counts = Array.fill(26)(0)
    var length = 0
    val chars = s.toCharArray

    var index = 0
    while (index < chars.length) {
      if (index > 0 && (chars(index) - chars(index - 1) + 26) % 26 == 1) {
        length += 1
      } else {
        length = 1
      }
      val position = chars(index) - 'a'
      counts(position) = math.max(counts(position), length)
      index += 1
    }

    counts.sum
  }
}
