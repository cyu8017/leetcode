// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

object Solution {
  def minTime(n: Int, k: Int, m: Int, time: Array[Int], mul: Array[Double]): Double = {
    val t = time.clone()
    java.util.Arrays.sort(t)
    var total = 0.0
    var stage = 0
    var left = n
    while (left > 0) {
      val take = math.min(k, left)
      val slow = t(left - 1)
      total += slow.toDouble * mul(stage % m)
      left -= take
      stage += 1
      if (left > 0) {
        total += t(0).toDouble * mul(stage % m)
        stage += 1
      }
    }
    total
  }
}
