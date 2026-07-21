// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

object Solution {
  def subsetXORSum(nums: Array[Int]): Int = {
    var bits = 0
    for (num <- nums) bits |= num
    var total = 0
    var bit = 1
    while (bit <= bits) {
      if ((bits & bit) != 0) total += bit
      bit <<= 1
    }
    total << (nums.length - 1)
  }
}
