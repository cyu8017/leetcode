// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

object Solution {
  def canAliceWin(n: Int): Boolean = {
    var nn = n
    var take = 10
    var alice = true
    while (nn >= take && take > 0) {
      nn -= take
      take -= 1
      alice = !alice
    }
    !alice
  }
}
