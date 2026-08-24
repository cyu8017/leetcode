// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

object Solution {
  def minimumSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val inf = 1 << 30
    val d = new java.util.HashMap[Integer, Integer]()
    var i = 0
    while (i < nums2.length) {
      d.putIfAbsent(nums2(i), i)
      i += 1
    }
    var ans = inf
    i = 0
    while (i < nums1.length) {
      val j = d.get(nums1(i))
      if (j != null) ans = math.min(ans, i + j.intValue())
      i += 1
    }
    if (ans == inf) -1 else ans
  }
}
