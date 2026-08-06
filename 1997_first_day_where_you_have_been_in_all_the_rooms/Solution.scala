// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

object Solution {
  def firstDayBeenInAllRooms(nextVisit: Array[Int]): Int = {
    val MOD = 1000000007
    val n = nextVisit.length
    val dp = Array.ofDim[Int](n)
    for (i <- 1 until n) {
      dp(i) = ((2L * dp(i - 1) - dp(nextVisit(i - 1)) + 2) % MOD).toInt
      if (dp(i) < 0) dp(i) += MOD
    }
    dp(n - 1)
  }
}
