// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

object Solution {
  def maxSelectedElements(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val dp = scala.collection.mutable.HashMap[Int, Int]()
    var ans = 0
    for (num <- nums) {
      val dn = dp.getOrElse(num, 0)
      val dnm1 = dp.getOrElse(num - 1, 0)
      dp(num + 1) = dn + 1
      dp(num) = dnm1 + 1
      ans = math.max(ans, math.max(dp(num), dp(num + 1)))
    }
    ans
  }
}
