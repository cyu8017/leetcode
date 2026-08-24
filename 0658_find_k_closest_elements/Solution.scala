// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

object Solution {
  def findClosestElements(arr: Array[Int], k: Int, x: Int): List[Int] = {
    var left = 0
    var right = arr.length - k
    while (left < right) {
      val mid = left + (right - left) / 2
      if (x - arr(mid) > arr(mid + k) - x) left = mid + 1
      else right = mid
    }
    arr.slice(left, left + k).toList
  }
}
