// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

object Solution {
  def escapeGhosts(ghosts: Array[Array[Int]], target: Array[Int]): Boolean = {
    val targetDist = math.abs(target(0)) + math.abs(target(1))
    !ghosts.exists { g =>
      math.abs(g(0) - target(0)) + math.abs(g(1) - target(1)) <= targetDist
    }
  }
}
