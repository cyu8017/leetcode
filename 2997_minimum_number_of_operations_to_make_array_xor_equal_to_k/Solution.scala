// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var xorr = 0
    for (v <- nums) xorr ^= v
    var diff = xorr ^ k
    var ans = 0
    while (diff > 0) {
      ans += diff & 1
      diff >>= 1
    }
    ans
  }
}
