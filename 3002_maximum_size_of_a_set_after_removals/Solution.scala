// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

object Solution {
  def maximumSetSize(nums1: Array[Int], nums2: Array[Int]): Int = {
    val s1 = nums1.toSet
    val s2 = nums2.toSet
    var a = 0
    var b = 0
    var c = 0
    for (x <- s1) if (!s2.contains(x)) a += 1
    for (x <- s2) {
      if (!s1.contains(x)) b += 1
      else c += 1
    }
    val n = nums1.length
    a = math.min(a, n / 2)
    b = math.min(b, n / 2)
    math.min(a + b + c, n)
  }
}
