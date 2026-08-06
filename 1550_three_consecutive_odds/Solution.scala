// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

object Solution {
  def threeConsecutiveOdds(arr: Array[Int]): Boolean = {
    var run = 0
    for (value <- arr) {
      run = if ((value & 1) == 1) run + 1 else 0
      if (run == 3) return true
    }
    false
  }
}
