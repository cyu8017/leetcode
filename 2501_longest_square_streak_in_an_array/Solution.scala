// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

object Solution {
  def longestSquareStreak(nums: Array[Int]): Int = {
    val set = scala.collection.mutable.HashSet.empty[Long]
    var i = 0
    while (i < nums.length) {
      set += nums(i).toLong
      i += 1
    }
    var best = -1
    i = 0
    while (i < nums.length) {
      var cur = nums(i).toLong
      if (set.contains(cur)) {
        var length = 0
        var cont = true
        while (cont && set.contains(cur)) {
          length += 1
          set -= cur
          if (cur > 100000) cont = false
          else cur = cur * cur
        }
        if (length >= 2 && length > best) best = length
      }
      i += 1
    }
    best
  }
}
