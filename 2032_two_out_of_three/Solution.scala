// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

object Solution {
  def twoOutOfThree(nums1: Array[Int], nums2: Array[Int], nums3: Array[Int]): Array[Int] = {
    val s0 = nums1.toSet
    val s1 = nums2.toSet
    val s2 = nums3.toSet
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var v = 1
    while (v <= 100) {
      val c = (if (s0.contains(v)) 1 else 0) + (if (s1.contains(v)) 1 else 0) + (if (s2.contains(v)) 1 else 0)
      if (c >= 2) ans += v
      v += 1
    }
    ans.toArray
  }
}
