// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

object Solution {
  def canMakePaliQueries(s: String, queries: Array[Array[Int]]): Array[Boolean] = {
    val prefix = Array.ofDim[Int](s.length + 1)
    var mask = 0
    for (i <- s.indices) {
      mask ^= 1 << (s(i) - 'a')
      prefix(i + 1) = mask
    }
    queries.map { q =>
      val bits = Integer.bitCount(prefix(q(1) + 1) ^ prefix(q(0)))
      bits / 2 <= q(2)
    }
  }
}
