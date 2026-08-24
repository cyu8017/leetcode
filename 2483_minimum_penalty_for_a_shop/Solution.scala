// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

object Solution {
  def bestClosingTime(customers: String): Int = {
    val n = customers.length
    var penalty = 0
    var i = 0
    while (i < n) {
      if (customers.charAt(i) == 'Y') penalty += 1
      i += 1
    }
    var best = penalty
    var ans = 0
    i = 0
    while (i < n) {
      if (customers.charAt(i) == 'Y') penalty -= 1
      else penalty += 1
      if (penalty < best) {
        best = penalty
        ans = i + 1
      }
      i += 1
    }
    ans
  }
}
