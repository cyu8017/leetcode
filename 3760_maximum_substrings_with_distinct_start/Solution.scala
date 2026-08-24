// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

object Solution {
  def maxDistinct(s: String): Int = {
    val cnt = new Array[Int](26)
    var ans = 0
    s.foreach { c =>
      cnt(c - 'a') += 1
      if (cnt(c - 'a') == 1) ans += 1
    }
    ans
  }
}
