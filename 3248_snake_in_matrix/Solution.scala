// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

object Solution {
  def finalPositionOfSnake(n: Int, commands: Array[String]): Int = {
    var x = 0
    var y = 0
    for (c <- commands) {
      c.charAt(0) match {
        case 'U' => x -= 1
        case 'D' => x += 1
        case 'L' => y -= 1
        case 'R' => y += 1
        case _ =>
      }
    }
    x * n + y
  }
}
