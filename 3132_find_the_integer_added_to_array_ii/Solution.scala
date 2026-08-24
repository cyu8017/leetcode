// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

object Solution {
  def minimumAddedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
    val a = nums1.sorted
    val b = nums2.sorted
    var ans = 1 << 30
    var t = 0
    while (t < 3) {
      val x = b(0) - a(t)
      if (ok(a, b, x)) ans = math.min(ans, x)
      t += 1
    }
    ans
  }

  private def ok(nums1: Array[Int], nums2: Array[Int], x: Int): Boolean = {
    var i = 0
    var j = 0
    var cnt = 0
    while (i < nums1.length && j < nums2.length) {
      if (nums2(j) - nums1(i) != x) cnt += 1
      else j += 1
      i += 1
    }
    cnt <= 2
  }
}
