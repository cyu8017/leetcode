// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

object Solution {
  def maximumLengthSubstring(s: String): Int = {
    var l = 0
    var ans = 0
    val cnt = new Array[Int](26)
    var r = 0
    while (r < s.length) {
      val idx = s.charAt(r) - 'a'
      cnt(idx) += 1
      while (cnt(idx) > 2) {
        cnt(s.charAt(l) - 'a') -= 1
        l += 1
      }
      ans = math.max(ans, r - l + 1)
      r += 1
    }
    ans
  }
}
