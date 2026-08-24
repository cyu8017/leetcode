// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

object Solution {
  def maxArea(height: Int, positions: Array[Int], directions: String): Long = {
    val n = positions.length
    val pos = positions.clone()
    val dir = directions.toCharArray
    var best = 0L
    var t = 0
    while (t <= 2 * height) {
      var sum = 0L
      var i = 0
      while (i < n) { sum += pos(i); i += 1 }
      if (sum > best) best = sum
      i = 0
      while (i < n) {
        if (dir(i) == 'U') {
          if (pos(i) == height) { dir(i) = 'D'; pos(i) -= 1 }
          else pos(i) += 1
        } else {
          if (pos(i) == 0) { dir(i) = 'U'; pos(i) += 1 }
          else pos(i) -= 1
        }
        i += 1
      }
      t += 1
    }
    best
  }
}
