// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

object Solution {
  def peakIndexInMountainArray(arr: Array[Int]): Int = {
    var lo = 0
    var hi = arr.length - 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (arr(mid) < arr(mid + 1)) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
