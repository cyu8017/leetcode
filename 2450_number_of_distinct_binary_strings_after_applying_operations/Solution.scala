// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

object Solution {
  def countDistinctStrings(s: String, k: Int): Int = {
    val mod = 1000000007
    val n = s.length
    var ans = 1
    var i = 0
    while (i < n - k + 1) {
      ans = (ans * 2L % mod).toInt
      i += 1
    }
    ans
  }
}
