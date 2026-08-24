// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

object Solution {
  def minimumKeypresses(s: String): Int = {
    val freq = Array.fill(26)(0)
    var i = 0
    while (i < s.length) {
      freq(s.charAt(i) - 'a') += 1
      i += 1
    }
    val sorted = freq.sorted(Ordering[Int].reverse)
    var ans = 0
    i = 0
    while (i < 26) {
      if (sorted(i) == 0) return ans
      ans += sorted(i) * (i / 9 + 1)
      i += 1
    }
    ans
  }
}
