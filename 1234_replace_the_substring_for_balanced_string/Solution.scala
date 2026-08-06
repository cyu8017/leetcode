// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

object Solution {
  def balancedString(s: String): Int = {
    val count = scala.collection.mutable.Map('Q' -> 0, 'W' -> 0, 'E' -> 0, 'R' -> 0)
    for (ch <- s) count(ch) += 1
    val limit = s.length / 4
    val n = s.length
    var left = 0
    var answer = n
    for (right <- s.indices) {
      count(s(right)) -= 1
      while (left < n && "QWER".forall(c => count(c) <= limit)) {
        answer = math.min(answer, right - left + 1)
        count(s(left)) += 1
        left += 1
      }
    }
    answer
  }
}
