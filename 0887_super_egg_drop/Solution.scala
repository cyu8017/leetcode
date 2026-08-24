// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

object Solution {
  def superEggDrop(k: Int, n: Int): Int = {
    val dp = Array.fill(k + 1)(0)
    var moves = 0
    while (dp(k) < n) {
      moves += 1
      var eggs = k
      while (eggs >= 1) {
        dp(eggs) = dp(eggs) + dp(eggs - 1) + 1
        eggs -= 1
      }
    }
    moves
  }
}
