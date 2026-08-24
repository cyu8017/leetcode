// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

object Solution {
  def numPermsDISequence(s: String): Int = {
    val MOD = 1000000007
    val n = s.length
    var dp = Array.fill(n + 1)(1)
    var i = 1
    while (i <= n) {
      val newDp = Array.ofDim[Int](n + 1)
      if (s.charAt(i - 1) == 'I') {
        var postfix = 0
        var j = n - i
        while (j >= 0) {
          postfix = (postfix + dp(j + 1)) % MOD
          newDp(j) = postfix
          j -= 1
        }
      } else {
        var prefix = 0
        var j = 0
        while (j <= n - i) {
          prefix = (prefix + dp(j)) % MOD
          newDp(j) = prefix
          j += 1
        }
      }
      dp = newDp
      i += 1
    }
    dp(0)
  }
}
