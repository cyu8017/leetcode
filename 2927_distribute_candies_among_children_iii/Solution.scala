// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

object Solution {
  def distributeCandies(n: Int, limit: Int): Long = {
    var ans = comb(n + 2L)
    ans -= 3 * comb((n - limit).toLong + 1)
    ans += 3 * comb((n - 2 * (limit + 1)).toLong + 2)
    ans -= comb((n - 3 * (limit + 1)).toLong + 2)
    if (ans < 0) 0 else ans
  }

  private def comb(x: Long): Long = if (x < 2) 0 else x * (x - 1) / 2
}
