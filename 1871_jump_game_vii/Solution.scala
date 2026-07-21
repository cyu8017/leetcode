// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

object Solution {
  def canReach(s: String, minJump: Int, maxJump: Int): Boolean = {
    val n = s.length
    val reachable = Array.fill(n)(false)
    reachable(0) = true
    val prefix = Array.fill(n + 1)(0)
    for (i <- 0 until n) {
      if (i > 0 && s(i) == '0') {
        val left = math.max(0, i - maxJump)
        val right = i - minJump
        if (right >= left && prefix(right + 1) - prefix(left) > 0) {
          reachable(i) = true
        }
      }
      prefix(i + 1) = prefix(i) + (if (reachable(i)) 1 else 0)
    }
    reachable(n - 1)
  }
}
