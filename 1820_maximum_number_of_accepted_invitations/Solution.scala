// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

object Solution {
  def maximumInvitations(grid: Array[Array[Int]]): Int = {
    val boys = grid.length
    val girls = grid(0).length
    val matchGirl = Array.fill(girls)(-1)

    def dfs(boy: Int, seen: Array[Boolean]): Boolean = {
      for (girl <- 0 until girls if grid(boy)(girl) == 1 && !seen(girl)) {
        seen(girl) = true
        if (matchGirl(girl) == -1 || dfs(matchGirl(girl), seen)) {
          matchGirl(girl) = boy
          return true
        }
      }
      false
    }

    var ans = 0
    for (boy <- 0 until boys) {
      if (dfs(boy, Array.fill(girls)(false))) ans += 1
    }
    ans
  }
}
