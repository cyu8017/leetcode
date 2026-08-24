// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

object Solution {
  def addedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
    var min1 = nums1(0)
    var min2 = nums2(0)
    nums1.foreach(x => min1 = math.min(min1, x))
    nums2.foreach(x => min2 = math.min(min2, x))
    min2 - min1
  }
}
