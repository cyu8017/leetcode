// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

object Solution {
  def countWays(nums: Array[Int]): Int = {
    val a = nums.sorted
    val n = a.length
    var ans = 0
    if (a(0) > 0) ans += 1
    for (i <- 0 until n) {
      val selected = i + 1
      if (selected > a(i) && (i == n - 1 || selected < a(i + 1))) ans += 1
    }
    ans
  }
}
