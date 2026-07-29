// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

object Solution {
  def fixedPoint(arr: Array[Int]): Int = {
    var lo = 0
    var hi = arr.length - 1
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (arr(mid) == mid) { ans = mid; hi = mid - 1 }
      else if (arr(mid) < mid) lo = mid + 1
      else hi = mid - 1
    }
    ans
  }
}
