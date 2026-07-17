// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

object Solution {
  def countPairs(deliciousness: Array[Int]): Int = {
    val mod = 1000000007L
    val seen = scala.collection.mutable.Map.empty[Int, Long]
    var ans = 0L
    for (value <- deliciousness) {
      for (power <- 0 until 22) {
        seen.get((1 << power) - value).foreach(ans += _)
      }
      seen(value) = seen.getOrElse(value, 0L) + 1L
    }
    (ans % mod).toInt
  }
}
