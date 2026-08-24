// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

object Solution {
  def minCost(nums1: Array[Int], nums2: Array[Int]): Int = {
    val cnt2 = scala.collection.mutable.Map.empty[Int, Int]
    nums2.foreach { x => cnt2(x) = cnt2.getOrElse(x, 0) + 1 }
    val cnt1 = scala.collection.mutable.Map.empty[Int, Int]
    nums1.foreach { x =>
      val c = cnt2.getOrElse(x, 0)
      if (c > 0) cnt2(x) = c - 1
      else cnt1(x) = cnt1.getOrElse(x, 0) + 1
    }
    var ans = 0
    cnt1.values.foreach { v =>
      if (v % 2 == 1) return -1
      ans += v / 2
    }
    cnt2.values.foreach { v =>
      if (v % 2 == 1) return -1
    }
    ans
  }
}
