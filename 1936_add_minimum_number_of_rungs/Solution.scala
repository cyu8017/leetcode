// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

object Solution {
  def addRungs(rungs: Array[Int], dist: Int): Int = {
    var prev = 0
    var ans = 0
    for (r <- rungs) {
      val gap = r - prev
      if (gap > dist) ans += (gap - 1) / dist
      prev = r
    }
    ans
  }
}
