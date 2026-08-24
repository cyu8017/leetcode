// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

object Solution {
  def uniformArray(nums1: Array[Int]): Boolean = {
    var mn = Int.MaxValue
    nums1.foreach { x => if (x % 2 == 1 && x < mn) mn = x }
    nums1.foreach { x =>
      if (x % 2 == 0 && mn != Int.MaxValue && x < mn) return false
    }
    true
  }
}
