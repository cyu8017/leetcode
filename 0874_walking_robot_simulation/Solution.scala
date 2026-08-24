// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

object Solution {
  def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]): Int = {
    def encode(x: Int, y: Int): Long = ((x + 30000).toLong << 20) | (y + 30000)
    val blocked = obstacles.map(o => encode(o(0), o(1))).toSet
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var x = 0
    var y = 0
    var d = 0
    var best = 0
    commands.foreach { cmd =>
      if (cmd == -1) d = (d + 1) % 4
      else if (cmd == -2) d = (d + 3) % 4
      else {
        val dx = dirs(d)(0)
        val dy = dirs(d)(1)
        var step = 0
        var cont = true
        while (step < cmd && cont) {
          val nx = x + dx
          val ny = y + dy
          if (blocked.contains(encode(nx, ny))) cont = false
          else {
            x = nx
            y = ny
          }
          step += 1
        }
        best = math.max(best, x * x + y * y)
      }
    }
    best
  }
}
