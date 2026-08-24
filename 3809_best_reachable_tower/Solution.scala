// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

object Solution {
  def bestTower(towers: Array[Array[Int]], center: Array[Int], radius: Int): Array[Int] = {
    val cx = center(0)
    val cy = center(1)
    var idx = -1
    var i = 0
    while (i < towers.length) {
      val x = towers(i)(0)
      val y = towers(i)(1)
      val q = towers(i)(2)
      val dist = math.abs(x - cx) + math.abs(y - cy)
      if (dist <= radius) {
        if (idx == -1 || towers(idx)(2) < q ||
            (towers(idx)(2) == q &&
             (x < towers(idx)(0) || (x == towers(idx)(0) && y < towers(idx)(1))))) {
          idx = i
        }
      }
      i += 1
    }
    if (idx == -1) Array(-1, -1) else Array(towers(idx)(0), towers(idx)(1))
  }
}
