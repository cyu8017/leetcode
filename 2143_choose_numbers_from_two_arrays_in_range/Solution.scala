// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

object Solution {
  def countSubranges(nums1: Array[Int], nums2: Array[Int]): Int = {
    val Mod = 1000000007
    val n = nums1.length
    var ans = 0
    var dp = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < n) {
      val ndp = scala.collection.mutable.Map.empty[Int, Int]
      ndp(nums1(i)) = (ndp.getOrElse(nums1(i), 0) + 1) % Mod
      ndp(-nums2(i)) = (ndp.getOrElse(-nums2(i), 0) + 1) % Mod
      dp.foreach { case (diff, cnt) =>
        ndp(diff + nums1(i)) = (ndp.getOrElse(diff + nums1(i), 0) + cnt) % Mod
        ndp(diff - nums2(i)) = (ndp.getOrElse(diff - nums2(i), 0) + cnt) % Mod
      }
      dp = ndp
      ans = (ans + dp.getOrElse(0, 0)) % Mod
      i += 1
    }
    ans
  }
}
