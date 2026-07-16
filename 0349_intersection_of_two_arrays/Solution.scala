// LeetCode 0349 - Intersection of Two Arrays

// https://leetcode.com/problems/intersection-of-two-arrays/



object Solution {

  def intersection(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {

    nums1.toSet.intersect(nums2.toSet).toArray

  }

}
