// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

object Solution {
  def isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean = {
    val need = math.max(math.abs(sx - fx), math.abs(sy - fy))
    if (need == 0) t != 1 else t >= need
  }
}
