// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

object Solution {
  def xorBeauty(nums: Array[Int]): Int = {
    var ans = 0
    nums.foreach(x => ans ^= x)
    ans
  }
}
