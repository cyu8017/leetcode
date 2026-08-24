// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

object Solution {
  def minMoves(target: Int, maxDoubles: Int): Int = {
    var t = target
    var d = maxDoubles
    var ans = 0
    while (t > 1 && d > 0) {
      if (t % 2 != 0) { t -= 1; ans += 1 }
      else { t /= 2; d -= 1; ans += 1 }
    }
    ans + t - 1
  }
}
