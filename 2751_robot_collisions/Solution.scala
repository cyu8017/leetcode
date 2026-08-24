// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

object Solution {
  def survivedRobotsHealths(positions: Array[Int], healths: Array[Int], directions: String): List[Int] = {
    val n = positions.length
    val idx = (0 until n).toArray.sortBy(positions)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    idx.foreach { i =>
      val cur = Array(i, healths(i), directions.charAt(i).toInt)
      var add = true
      while (add && stack.nonEmpty && stack.last(2) == 'R' && cur(2) == 'L') {
        val top = stack.last
        if (top(1) == cur(1)) {
          stack.remove(stack.length - 1)
          cur(1) = 0
          add = false
        } else if (top(1) > cur(1)) {
          top(1) -= 1
          cur(1) = 0
          add = false
        } else {
          cur(1) -= 1
          stack.remove(stack.length - 1)
        }
      }
      if (cur(1) > 0) stack += cur
    }
    val alive = stack.map(r => r(0) -> r(1)).toMap
    (0 until n).flatMap(i => alive.get(i)).toList
  }
}
