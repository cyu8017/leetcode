// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

object Solution {
  def numberOfPermutations(n: Int, requirements: Array[Array[Int]]): Int = {
    val req = Array.fill(n)(-1)
    for (r <- requirements) req(r(0)) = r(1)
    if (req(0) > 0) return 0
    req(0) = 0
    var m = 0
    for (v <- req) m = math.max(m, v)
    val mod = 1000000007
    val f = Array.ofDim[Int](n, m + 1)
    f(0)(0) = 1
    var i = 1
    while (i < n) {
      var l = 0
      var r = m
      if (req(i) >= 0) { l = req(i); r = req(i) }
      var j = l
      while (j <= r) {
        var k = 0
        while (k <= math.min(i, j)) {
          f(i)(j) = (f(i)(j) + f(i - 1)(j - k)) % mod
          k += 1
        }
        j += 1
      }
      i += 1
    }
    f(n - 1)(req(n - 1))
  }
}
