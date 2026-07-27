// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

object Solution {
  def maxRepeating(sequence: String, word: String): Int = {
    var k = 0
    while (sequence.contains(word * (k + 1))) k += 1
    k
  }
}
