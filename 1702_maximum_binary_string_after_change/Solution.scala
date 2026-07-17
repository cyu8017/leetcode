// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

object Solution {
  def maximumBinaryString(binary: String): String = {
    val zeros = binary.count(_ == '0')
    if (zeros <= 1) {
      return binary
    }
    val first = binary.indexOf('0')
    val n = binary.length
    "1" * (first + zeros - 1) + "0" + "1" * (n - first - zeros)
  }
}
