// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

object Solution {
  def winnerOfGame(colors: String): Boolean = {
    var a = 0
    var b = 0
    var i = 1
    while (i + 1 < colors.length) {
      if (colors.charAt(i - 1) == colors.charAt(i) && colors.charAt(i) == colors.charAt(i + 1)) {
        if (colors.charAt(i) == 'A') a += 1
        else b += 1
      }
      i += 1
    }
    a > b
  }
}
