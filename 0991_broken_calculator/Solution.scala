// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

object Solution {
  def brokenCalc(startValue: Int, target: Int): Int = {
    var t = target
    var ans = 0
    while (t > startValue) {
      if (t % 2 == 1) t += 1
      else t /= 2
      ans += 1
    }
    ans + startValue - t
  }
}
