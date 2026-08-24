// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

object Solution {
  def distributeCandies(n: Int, limit: Int): Long = {
    var ans = comb2(n)
    ans -= 3 * comb2(n - (limit + 1))
    ans += 3 * comb2(n - 2 * (limit + 1))
    ans -= comb2(n - 3 * (limit + 1))
    ans
  }

  private def comb2(x: Long): Long = if (x < 0) 0 else (x + 1) * (x + 2) / 2
}
