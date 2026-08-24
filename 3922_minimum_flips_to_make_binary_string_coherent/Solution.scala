// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

object Solution {
  def minFlips(s: String): Int = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    var answer = ones
    if (ones > 0) answer = ones - 1
    val zeros = s.length - ones
    answer = math.min(answer, zeros)
    if (s.length >= 2) {
      var cost = 0
      var i = 0
      while (i < s.length) {
        val want = if (i == 0 || i == s.length - 1) '1' else '0'
        if (s.charAt(i) != want) cost += 1
        i += 1
      }
      answer = math.min(answer, cost)
    }
    answer
  }
}
