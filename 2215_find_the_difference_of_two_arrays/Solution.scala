// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

object Solution {
  def findDifference(nums1: Array[Int], nums2: Array[Int]): List[List[Int]] = {
    val s1 = scala.collection.mutable.HashSet.empty[Int]
    val s2 = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums1) s1 += x
    for (x <- nums2) s2 += x
    val a = scala.collection.mutable.ListBuffer.empty[Int]
    val b = scala.collection.mutable.ListBuffer.empty[Int]
    for (x <- s1 if !s2.contains(x)) a += x
    for (x <- s2 if !s1.contains(x)) b += x
    List(a.toList, b.toList)
  }
}
