// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def selfDivisiblePermutationCount(n: Int): Int = {
    var ans = 0
    val used = Array.ofDim[Boolean](n + 1)
    def dfs(pos: Int): Unit = {
      if (pos > n) { ans += 1; return }
      var v = 1
      while (v <= n) {
        if (!used(v) && gcd(v, pos) == 1) {
          used(v) = true
          dfs(pos + 1)
          used(v) = false
        }
        v += 1
      }
    }
    dfs(1)
    ans
  }
}
