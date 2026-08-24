// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

object Solution {
  def minimumTotalCost(nums1: Array[Int], nums2: Array[Int]): Long = {
    val n = nums1.length
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0L
    var same = 0
    var i = 0
    while (i < n) {
      if (nums1(i) == nums2(i)) {
        same += 1
        freq(nums1(i)) = freq.getOrElse(nums1(i), 0) + 1
        ans += i
      }
      i += 1
    }
    var maxFreq = 0
    var maxVal = 0
    freq.foreach { case (k, v) =>
      if (v > maxFreq) {
        maxFreq = v
        maxVal = k
      }
    }
    var need = maxFreq * 2 - same
    if (need <= 0) return ans
    i = 0
    while (i < n && need > 0) {
      if (nums1(i) != nums2(i) && nums1(i) != maxVal && nums2(i) != maxVal) {
        ans += i
        need -= 1
      }
      i += 1
    }
    if (need > 0) -1 else ans
  }
}
