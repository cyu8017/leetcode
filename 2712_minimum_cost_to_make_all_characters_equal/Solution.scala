// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

object Solution {
  def minimumCost(s: String): Long = {
    val n = s.length
    var ans = 0L
    var i = 1
    while (i < n) {
      if (s.charAt(i) != s.charAt(i - 1)) ans += math.min(i, n - i)
      i += 1
    }
    ans
  }
}
