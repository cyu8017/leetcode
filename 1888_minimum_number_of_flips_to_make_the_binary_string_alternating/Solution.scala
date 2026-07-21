// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

object Solution {
  def minFlips(s: String): Int = {
    val n = s.length
    val doubled = s + s
    var alt0 = 0
    var alt1 = 0
    for (i <- 0 until n) {
      val expect0 = if (i % 2 == 0) '0' else '1'
      val expect1 = if (i % 2 == 0) '1' else '0'
      if (doubled(i) != expect0) alt0 += 1
      if (doubled(i) != expect1) alt1 += 1
    }
    var answer = math.min(alt0, alt1)
    for (i <- 0 until n) {
      val expect0i = if (i % 2 == 0) '0' else '1'
      val expect0n = if ((i + n) % 2 == 0) '0' else '1'
      if (doubled(i) != expect0i) alt0 -= 1
      if (doubled(i + n) != expect0n) alt0 += 1

      val expect1i = if (i % 2 == 0) '1' else '0'
      val expect1n = if ((i + n) % 2 == 0) '1' else '0'
      if (doubled(i) != expect1i) alt1 -= 1
      if (doubled(i + n) != expect1n) alt1 += 1

      answer = math.min(answer, math.min(alt0, alt1))
    }
    answer
  }
}
