// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

object Solution {
  def advantageCount(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val sorted1 = nums1.sorted
    val dq = scala.collection.mutable.ArrayDeque(sorted1: _*)
    val ans = Array.ofDim[Int](nums1.length)
    val indexed = nums2.indices.map(i => (nums2(i), i)).sortBy(-_._1)
    indexed.foreach { case (value, i) =>
      if (dq.last > value) ans(i) = dq.removeLast()
      else ans(i) = dq.removeHead()
    }
    ans
  }
}
