// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

object Solution {
  def judgeCircle(moves: String): Boolean = {
    var x = 0
    var y = 0
    var i = 0
    while (i < moves.length) {
      val move = moves.charAt(i)
      if (move == 'U') y += 1
      else if (move == 'D') y -= 1
      else if (move == 'L') x -= 1
      else if (move == 'R') x += 1
      i += 1
    }
    x == 0 && y == 0
  }
}
