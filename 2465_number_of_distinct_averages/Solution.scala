// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

object Solution {
  def distinctAverages(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var l = 0
    var r = nums.length - 1
    while (l < r) {
      seen += nums(l) + nums(r)
      l += 1
      r -= 1
    }
    seen.size
  }
}
