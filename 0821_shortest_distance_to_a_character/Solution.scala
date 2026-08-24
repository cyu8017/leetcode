// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

object Solution {
  def shortestToChar(s: String, c: Char): Array[Int] = {
    val n = s.length
    val ans = Array.ofDim[Int](n)
    var prev = -n
    var i = 0
    while (i < n) {
      if (s.charAt(i) == c) prev = i
      ans(i) = i - prev
      i += 1
    }
    prev = 2 * n
    i = n - 1
    while (i >= 0) {
      if (s.charAt(i) == c) prev = i
      ans(i) = math.min(ans(i), prev - i)
      i -= 1
    }
    ans
  }
}
