// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

object Solution {
  def findKthBit(n: Int, k: Int): Char = {
    var invert = false
    var length = (1 << n) - 1
    var kk = k
    while (kk != 1) {
      val middle = length / 2 + 1
      if (kk == middle) return if (invert) '0' else '1'
      if (kk > middle) {
        kk = length - kk + 1
        invert = !invert
      }
      length /= 2
    }
    if (invert) '1' else '0'
  }
}
