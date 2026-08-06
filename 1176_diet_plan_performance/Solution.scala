// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

object Solution {
  def dietPlanPerformance(calories: Array[Int], k: Int, lower: Int, upper: Int): Int = {
    var window = calories.take(k).sum
    var ans = 0
    if (window < lower) ans -= 1
    else if (window > upper) ans += 1
    for (i <- k until calories.length) {
      window += calories(i) - calories(i - k)
      if (window < lower) ans -= 1
      else if (window > upper) ans += 1
    }
    ans
  }
}
