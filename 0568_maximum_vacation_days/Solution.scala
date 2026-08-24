// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

object Solution {
  def maxVacationDays(flights: Array[Array[Int]], days: Array[Array[Int]]): Int = {
    val cities = flights.length
    val weeks = days(0).length
    val NEG = -1000000000
    var dp = Array.fill(cities)(NEG)
    dp(0) = 0
    var week = 0
    while (week < weeks) {
      val nxt = Array.fill(cities)(NEG)
      var city = 0
      while (city < cities) {
        if (dp(city) != NEG) {
          var dest = 0
          while (dest < cities) {
            if (dest == city || flights(city)(dest) == 1) {
              nxt(dest) = math.max(nxt(dest), dp(city) + days(dest)(week))
            }
            dest += 1
          }
        }
        city += 1
      }
      dp = nxt
      week += 1
    }
    var best = NEG
    dp.foreach(v => best = math.max(best, v))
    best
  }
}
