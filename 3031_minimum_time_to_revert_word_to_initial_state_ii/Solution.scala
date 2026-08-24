// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

object Solution {
  private class Hashing(word: String, bas: Long, mod: Long) {
    val n = word.length
    val p = Array.ofDim[Long](n + 1)
    val h = Array.ofDim[Long](n + 1)
    p(0) = 1
    var i = 1
    while (i <= n) {
      p(i) = p(i - 1) * bas % mod
      h(i) = (h(i - 1) * bas + (word.charAt(i - 1) - 'a')) % mod
      i += 1
    }
    def query(l: Int, r: Int): Long =
      (h(r) - h(l - 1) * p(r - l + 1) % mod + mod) % mod
  }

  def minimumTimeToInitialState(word: String, k: Int): Int = {
    val hashing = new Hashing(word, 13331, 998244353)
    val n = word.length
    var i = k
    while (i < n) {
      if (hashing.query(1, n - i) == hashing.query(i + 1, n)) return i / k
      i += k
    }
    (n + k - 1) / k
  }
}
