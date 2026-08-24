// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

object Solution {
  def kInversePairs(n: Int, k: Int): Int = {
    val mod = 1000000007
    var dp = Array.fill(k + 1)(0)
    dp(0) = 1
    var size = 1
    while (size <= n) {
      val nxt = Array.fill(k + 1)(0)
      var prefix = 0L
      var pairs = 0
      while (pairs <= k) {
        prefix = (prefix + dp(pairs)) % mod
        if (pairs >= size) prefix = (prefix - dp(pairs - size) + mod) % mod
        nxt(pairs) = prefix.toInt
        pairs += 1
      }
      dp = nxt
      size += 1
    }
    dp(k)
  }
}
