// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

object Solution {
  def soupServings(n: Int): Double = {
    if (n >= 4800) return 1.0
    val units = (n + 24) / 25
    val memo = scala.collection.mutable.Map.empty[Long, Double]
    def dp(a: Int, b: Int): Double = {
      if (a <= 0 && b <= 0) return 0.5
      if (a <= 0) return 1.0
      if (b <= 0) return 0.0
      val key = (a.toLong << 16) | b
      memo.get(key) match {
        case Some(v) => v
        case None =>
          val v = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
          memo(key) = v
          v
      }
    }
    dp(units, units)
  }
}
