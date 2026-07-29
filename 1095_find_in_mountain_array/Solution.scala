// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

trait MountainArray {
  def get(index: Int): Int
  def length(): Int
}

object Solution {
  def findInMountainArray(target: Int, mountainArr: MountainArray): Int = {
    val n = mountainArr.length()
    var lo = 0
    var hi = n - 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mountainArr.get(mid) < mountainArr.get(mid + 1)) lo = mid + 1
      else hi = mid
    }
    val peak = lo
    lo = 0
    hi = peak
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      val v = mountainArr.get(mid)
      if (v == target) return mid
      if (v < target) lo = mid + 1 else hi = mid - 1
    }
    lo = peak + 1
    hi = n - 1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      val v = mountainArr.get(mid)
      if (v == target) return mid
      if (v > target) lo = mid + 1 else hi = mid - 1
    }
    -1
  }
}
