// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

object Solution {
  def widestPairOfIndices(nums1: Array[Int], nums2: Array[Int]): Int = {
    val first = scala.collection.mutable.Map(0 -> -1)
    var ans = 0
    var s = 0
    for (i <- nums1.indices) {
      s += nums1(i) - nums2(i)
      if (first.contains(s)) ans = math.max(ans, i - first(s))
      else first(s) = i
    }
    ans
  }
}
