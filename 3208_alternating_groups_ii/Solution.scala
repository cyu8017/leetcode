// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

object Solution {
  def numberOfAlternatingGroups(colors: Array[Int], k: Int): Int = {
    val n = colors.length
    var cnt = 0
    var ans = 0
    var i = 0
    while (i < n * 2) {
      if (i > 0 && colors(i % n) == colors((i - 1) % n)) cnt = 1
      else cnt += 1
      if (i >= n && cnt >= k) ans += 1
      i += 1
    }
    ans
  }
}
