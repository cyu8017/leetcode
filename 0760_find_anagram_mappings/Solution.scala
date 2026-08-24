// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

object Solution {
  def anagramMappings(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val positions = scala.collection.mutable.HashMap.empty[Int, scala.collection.mutable.Queue[Int]]
    var i = 0
    while (i < nums2.length) {
      positions.getOrElseUpdate(nums2(i), scala.collection.mutable.Queue.empty[Int]).enqueue(i)
      i += 1
    }
    val result = Array.ofDim[Int](nums1.length)
    i = 0
    while (i < nums1.length) {
      result(i) = positions(nums1(i)).dequeue()
      i += 1
    }
    result
  }
}
