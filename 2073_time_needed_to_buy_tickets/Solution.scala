// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

object Solution {
  def timeRequiredToBuy(tickets: Array[Int], k: Int): Int = {
    var ans = 0
    var i = 0
    while (i < tickets.length) {
      if (i <= k) ans += math.min(tickets(i), tickets(k))
      else ans += math.min(tickets(i), tickets(k) - 1)
      i += 1
    }
    ans
  }
}
