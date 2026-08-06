// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

object Solution {
  def distinctEchoSubstrings(text: String): Int = {
    val n = text.length
    val mod1 = 1000000007L
    val mod2 = 1000000009L
    val base = 911382323L
    val h1 = Array.ofDim[Long](n + 1)
    val h2 = Array.ofDim[Long](n + 1)
    val p1 = Array.fill(n + 1)(1L)
    val p2 = Array.fill(n + 1)(1L)
    for (i <- text.indices) {
      val code = text(i).toLong
      h1(i + 1) = (h1(i) * base + code) % mod1
      h2(i + 1) = (h2(i) * base + code) % mod2
      p1(i + 1) = p1(i) * base % mod1
      p2(i + 1) = p2(i) * base % mod2
    }
    def hashed(left: Int, right: Int): (Long, Long) = {
      val length = right - left
      val a = ((h1(right) - h1(left) * p1(length)) % mod1 + mod1) % mod1
      val b = ((h2(right) - h2(left) * p2(length)) % mod2 + mod2) % mod2
      (a, b)
    }
    val echoes = scala.collection.mutable.HashSet[(Int, Long, Long)]()
    for (half <- 1 to n / 2; left <- 0 to n - 2 * half) {
      if (hashed(left, left + half) == hashed(left + half, left + 2 * half)) {
        val (a, b) = hashed(left, left + 2 * half)
        echoes += ((2 * half, a, b))
      }
    }
    echoes.size
  }
}
