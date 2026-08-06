// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

object Solution {
  def countRoutes(locations: Array[Int], start: Int, finish: Int, fuel: Int): Int = {
    val MOD = 1000000007
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dp(city: Int, left: Int): Int = {
      memo.getOrElseUpdate((city, left), {
        var total = if (city == finish) 1 else 0
        for (nxt <- locations.indices if nxt != city) {
          val cost = math.abs(locations(city) - locations(nxt))
          if (cost <= left) total = (total + dp(nxt, left - cost)) % MOD
        }
        total
      })
    }
    dp(start, fuel)
  }
}
