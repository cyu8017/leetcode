// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

object Solution {
  def maxDistance(moves: String): Int = {
    var x = 0
    var y = 0
    var z = 0
    var i = 0
    while (i < moves.length) {
      val c = moves.charAt(i)
      if (c == 'U') x -= 1
      else if (c == 'D') x += 1
      else if (c == 'L') y -= 1
      else if (c == 'R') y += 1
      else z += 1
      i += 1
    }
    math.abs(x) + math.abs(y) + z
  }
}
