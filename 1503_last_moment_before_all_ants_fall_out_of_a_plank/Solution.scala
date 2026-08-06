// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

object Solution {
  def getLastMoment(n: Int, left: Array[Int], right: Array[Int]): Int = {
    val l = if (left.isEmpty) 0 else left.max
    val r = if (right.isEmpty) 0 else n - right.min
    math.max(l, r)
  }
}
