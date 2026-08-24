// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot(_width: Int, _height: Int) {
  private val w = _width
  private val h = _height
  private val peri = 2 * (w + h) - 4
  private var pos = 0
  private var moved = false

  private def getPosDir(): Array[Int] = {
    val p0 = pos
    if (p0 == 0) {
      if (!moved) Array(0, 0, 0)
      else Array(0, 0, 3)
    } else if (p0 <= w - 1) Array(p0, 0, 0)
    else {
      var p = p0 - (w - 1)
      if (p <= h - 1) Array(w - 1, p, 1)
      else {
        p -= h - 1
        if (p <= w - 1) Array(w - 1 - p, h - 1, 2)
        else {
          p -= w - 1
          Array(0, h - 1 - p, 3)
        }
      }
    }
  }

  def step(num: Int): Unit = {
    moved = true
    pos = (pos + num) % peri
  }

  def getPos(): Array[Int] = {
    val pd = getPosDir()
    Array(pd(0), pd(1))
  }

  def getDir(): String = {
    val names = Array("East", "North", "West", "South")
    names(getPosDir()(2))
  }
}
