// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

object Solution {
  def checkZeroOnes(s: String): Boolean = {
    var maxZeros = 0
    var maxOnes = 0
    var zeros = 0
    var ones = 0
    for (ch <- s) {
      if (ch == '0') {
        zeros += 1
        ones = 0
        maxZeros = math.max(maxZeros, zeros)
      } else {
        ones += 1
        zeros = 0
        maxOnes = math.max(maxOnes, ones)
      }
    }
    maxOnes > maxZeros
  }
}
