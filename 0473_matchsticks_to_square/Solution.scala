// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

object Solution {
  def makesquare(matchsticks: Array[Int]): Boolean = {
    if (matchsticks.isEmpty) return false
    val total = matchsticks.sum
    if (total % 4 != 0) return false
    val side = total / 4
    val sorted = matchsticks.sorted(Ordering[Int].reverse)

    def dfs(index: Int, sides: Array[Int]): Boolean = {
      if (index == sorted.length) {
        return sides(0) == side && sides.toSet.size == 1
      }
      val length = sorted(index)
      var sideIndex = 0
      while (sideIndex < 4) {
        if (sides(sideIndex) + length <= side) {
          if (sideIndex == 0 || sides(sideIndex) != sides(sideIndex - 1)) {
            sides(sideIndex) += length
            if (dfs(index + 1, sides)) {
              return true
            }
            sides(sideIndex) -= length
          }
        }
        sideIndex += 1
      }
      false
    }

    dfs(0, Array(0, 0, 0, 0))
  }
}
