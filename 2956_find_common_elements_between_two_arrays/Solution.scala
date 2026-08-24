// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

object Solution {
  def findIntersectionValues(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val s1 = nums1.toSet
    val s2 = nums2.toSet
    var a = 0
    var b = 0
    for (v <- nums1) if (s2.contains(v)) a += 1
    for (v <- nums2) if (s1.contains(v)) b += 1
    Array(a, b)
  }
}
