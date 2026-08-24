// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

object Solution {
  def maxDistance(s: String, k: Int): Int = {
    var ans = 0
    var lat = 0
    var lon = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'N') lat += 1
      else if (c == 'S') lat -= 1
      else if (c == 'E') lon += 1
      else lon -= 1
      val md = math.abs(lat) + math.abs(lon)
      val steps = i + 1
      var cur = md + 2 * k
      if (cur > steps) cur = steps
      if (cur > ans) ans = cur
      i += 1
    }
    ans
  }
}
