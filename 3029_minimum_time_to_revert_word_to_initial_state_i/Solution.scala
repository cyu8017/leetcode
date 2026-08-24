// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

object Solution {
  def minimumTimeToInitialState(word: String, k: Int): Int = {
    val n = word.length
    var i = k
    while (i < n) {
      if (word.substring(i) == word.substring(0, n - i)) return i / k
      i += k
    }
    (n + k - 1) / k
  }
}
