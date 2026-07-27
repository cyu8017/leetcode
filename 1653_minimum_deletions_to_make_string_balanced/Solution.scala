// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

object Solution {
  def minimumDeletions(s: String): Int = {
    var b = 0
    var ans = 0
    for (c <- s) {
      if (c == 'b') b += 1
      else ans = math.min(ans + 1, b)
    }
    ans
  }
}
