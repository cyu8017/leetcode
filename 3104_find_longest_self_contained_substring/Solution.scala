// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

object Solution {
  def maxSubstringLength(s: String): Int = {
    val first = Array.fill(26)(-1)
    val last = new Array[Int](26)
    val n = s.length
    var i = 0
    while (i < n) {
      val j = s.charAt(i) - 'a'
      if (first(j) == -1) first(j) = i
      last(j) = i
      i += 1
    }
    var ans = -1
    var k = 0
    while (k < 26) {
      i = first(k)
      if (i != -1) {
        var mx = last(k)
        var j = i
        var broken = false
        while (j < n && !broken) {
          val a = first(s.charAt(j) - 'a')
          val b = last(s.charAt(j) - 'a')
          if (a < i) broken = true
          else {
            mx = math.max(mx, b)
            if (mx == j && j - i + 1 < n) ans = math.max(ans, j - i + 1)
            j += 1
          }
        }
      }
      k += 1
    }
    ans
  }
}
