// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

object Solution {
  def distributeCandies(n: Int, limit: Int): Int = {
    var ans = 0
    for (i <- 0 to limit; j <- 0 to limit) {
      val k = n - i - j
      if (k >= 0 && k <= limit) ans += 1
    }
    ans
  }
}
