// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

object Solution {
  def xorAllNums(nums1: Array[Int], nums2: Array[Int]): Int = {
    var ans = 0
    if (nums2.length % 2 == 1) {
      var i = 0
      while (i < nums1.length) {
        ans ^= nums1(i)
        i += 1
      }
    }
    if (nums1.length % 2 == 1) {
      var i = 0
      while (i < nums2.length) {
        ans ^= nums2(i)
        i += 1
      }
    }
    ans
  }
}
