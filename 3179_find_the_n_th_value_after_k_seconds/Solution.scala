// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

object Solution {
  def valueAfterKSeconds(n: Int, k: Int): Int = {
    val mod = 1000000007
    val a = Array.fill(n)(1)
    var t = k
    while (t > 0) {
      var i = 1
      while (i < n) {
        a(i) = (a(i) + a(i - 1)) % mod
        i += 1
      }
      t -= 1
    }
    a(n - 1)
  }
}
