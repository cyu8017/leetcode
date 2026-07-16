// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

object Solution {
  def hammingDistance(x: Int, y: Int): Int =
    Integer.bitCount(x ^ y)
}
