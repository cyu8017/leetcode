// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

object Solution {
  def minSwaps(s: String): Int = {
    val zeros = s.count(_ == '0')
    val ones = s.length - zeros
    if (math.abs(zeros - ones) > 1) return -1

    def mismatches(start: Char): Int = {
      var count = 0
      for (i <- s.indices) {
        val expected = if (i % 2 == 0) start else (if (start == '0') '1' else '0')
        if (s(i) != expected) count += 1
      }
      count / 2
    }

    if (zeros == ones) math.min(mismatches('0'), mismatches('1'))
    else if (zeros > ones) mismatches('0')
    else mismatches('1')
  }
}
