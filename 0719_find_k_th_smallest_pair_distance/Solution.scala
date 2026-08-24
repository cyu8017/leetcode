// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

object Solution {
  def smallestDistancePair(nums: Array[Int], k: Int): Int = {
    val arr = nums.clone()
    scala.util.Sorting.quickSort(arr)
    var lo = 0
    var hi = arr(arr.length - 1) - arr(0)
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (countPairs(arr, mid) >= k) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def countPairs(nums: Array[Int], distance: Int): Int = {
    var count = 0
    var left = 0
    var right = 0
    while (right < nums.length) {
      while (nums(right) - nums(left) > distance) left += 1
      count += right - left
      right += 1
    }
    count
  }
}
