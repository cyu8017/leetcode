// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

object Solution {
  private def cost(startAt: Int, moveCost: Int, pushCost: Int, mins: Int, secs: Int): Int = {
    if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return Int.MaxValue / 2
    val s =
      if (mins > 0) mins.toString + ('0' + secs / 10).toChar + ('0' + secs % 10).toChar
      else secs.toString
    var cur = ('0' + startAt).toChar
    var ans = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c != cur) { ans += moveCost; cur = c }
      ans += pushCost
      i += 1
    }
    ans
  }

  def minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int = {
    val mins = targetSeconds / 60
    val secs = targetSeconds % 60
    var ans = cost(startAt, moveCost, pushCost, mins, secs)
    if (mins > 0) ans = math.min(ans, cost(startAt, moveCost, pushCost, mins - 1, secs + 60))
    ans
  }
}
