// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

object Solution {
  def equalizeWater(buckets: Array[Int], loss: Int): Double = {
    var lo = 0.0
    var hi = 0.0
    buckets.foreach(b => hi = math.max(hi, b.toDouble))
    var iter = 0
    while (iter < 60) {
      val mid = (lo + hi) / 2
      var have = 0.0
      var need = 0.0
      buckets.foreach { b =>
        if (b >= mid) have += b - mid
        else need += mid - b
      }
      if (have * (1.0 - loss / 100.0) >= need) lo = mid
      else hi = mid
      iter += 1
    }
    lo
  }
}
