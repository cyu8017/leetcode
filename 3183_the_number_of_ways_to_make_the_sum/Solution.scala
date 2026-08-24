// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

object Solution {
  def numberOfWays(n: Int): Int = {
    val mod = 1000000007
    val coins = Array(1, 2, 6)
    val f = new Array[Int](n + 1)
    f(0) = 1
    for (x <- coins) {
      var j = x
      while (j <= n) {
        f(j) = (f(j) + f(j - x)) % mod
        j += 1
      }
    }
    var ans = f(n)
    if (n >= 4) ans = (ans + f(n - 4)) % mod
    if (n >= 8) ans = (ans + f(n - 8)) % mod
    ans
  }
}
