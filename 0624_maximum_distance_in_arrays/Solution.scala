// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

object Solution {
  def maxDistance(arrays: List[List[Int]]): Int = {
    var minVal = arrays.head.head
    var maxVal = arrays.head.last
    var best = 0
    var i = 1
    while (i < arrays.size) {
      val arr = arrays(i)
      val first = arr.head
      val last = arr.last
      best = math.max(best, math.max(math.abs(last - minVal), math.abs(maxVal - first)))
      minVal = math.min(minVal, first)
      maxVal = math.max(maxVal, last)
      i += 1
    }
    best
  }
}
