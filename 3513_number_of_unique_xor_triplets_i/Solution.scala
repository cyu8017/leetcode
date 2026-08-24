// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

object Solution {
  def uniqueXorTriplets(nums: Array[Int]): Int = {
    val n = nums.length
    if (n <= 2) return n
    var x = n
    var len = 0
    while (x != 0) { len += 1; x >>= 1 }
    1 << len
  }
}
