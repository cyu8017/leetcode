// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

object Solution {
  def numberOfArrays(differences: Array[Int], lower: Int, upper: Int): Int = {
    var cur = 0L
    var mn = 0L
    var mx = 0L
    differences.foreach { d =>
      cur += d
      mn = math.min(mn, cur)
      mx = math.max(mx, cur)
    }
    val res = (upper.toLong - lower) - (mx - mn) + 1
    if (res < 0) 0 else res.toInt
  }
}
