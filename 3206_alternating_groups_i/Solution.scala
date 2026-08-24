// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

object Solution {
  def numberOfAlternatingGroups(colors: Array[Int]): Int = {
    val k = 3
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
