// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

object Solution {
  def isOneBitCharacter(bits: Array[Int]): Boolean = {
    var i = 0
    val n = bits.length
    while (i < n - 1) i += (if (bits(i) == 1) 2 else 1)
    i == n - 1
  }
}
