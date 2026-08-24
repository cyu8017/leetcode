// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

object Solution {
  def findPermutationDifference(s: String, t: String): Int = {
    val d = new Array[Int](26)
    var i = 0
    while (i < s.length) {
      d(s.charAt(i) - 'a') = i
      i += 1
    }
    var ans = 0
    i = 0
    while (i < t.length) {
      ans += math.abs(d(t.charAt(i) - 'a') - i)
      i += 1
    }
    ans
  }
}
