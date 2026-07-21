// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

object Solution {
  def getMaximumXor(nums: Array[Int], maximumBit: Int): Array[Int] = {
    val limit = (1 << maximumBit) - 1
    var current = 0
    for (num <- nums) current ^= num
    val result = Array.ofDim[Int](nums.length)
    var idx = 0
    for (i <- nums.indices.reverse) {
      result(idx) = current ^ limit
      idx += 1
      current ^= nums(i)
    }
    result
  }
}
