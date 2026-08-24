// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

object Solution {
  def minGroupsForValidAssignment(balls: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    balls.foreach(b => freq(b) = freq.getOrElse(b, 0) + 1)
    val counts = freq.values.toArray
    val minF = counts.min
    for (size <- minF to 1 by -1) {
      var ok = true
      var groups = 0
      counts.foreach { c =>
        if (ok) {
          val rem = c % (size + 1)
          val g2 = c / (size + 1)
          if (rem == 0) groups += g2
          else if (size - rem <= g2) groups += g2 + 1
          else ok = false
        }
      }
      if (ok) return groups
    }
    balls.length
  }
}
