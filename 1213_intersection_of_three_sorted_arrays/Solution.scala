// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

object Solution {
  def arraysIntersection(arr1: Array[Int], arr2: Array[Int], arr3: Array[Int]): List[Int] =
    (arr1.toSet & arr2.toSet & arr3.toSet).toList.sorted
}
