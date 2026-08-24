// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

object Solution {
  def rearrangeCharacters(s: String, target: String): Int = {
    val sc = new Array[Int](26)
    val tc = new Array[Int](26)
    var i = 0
    while (i < s.length) {
      sc(s.charAt(i) - 'a') += 1
      i += 1
    }
    i = 0
    while (i < target.length) {
      tc(target.charAt(i) - 'a') += 1
      i += 1
    }
    var ans = Int.MaxValue
    i = 0
    while (i < 26) {
      if (tc(i) != 0) ans = math.min(ans, sc(i) / tc(i))
      i += 1
    }
    ans
  }
}
