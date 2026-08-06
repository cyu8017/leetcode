// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

object Solution {
  def numberOfUniqueGoodSubsequences(binary: String): Int = {
    val MOD = 1000000007
    var ends0 = 0
    var ends1 = 0
    var has0 = false
    for (ch <- binary) {
      if (ch == '0') {
        has0 = true
        ends0 = (ends0 + ends1) % MOD
      } else {
        ends1 = (ends0 + ends1 + 1) % MOD
      }
    }
    (ends0 + ends1 + (if (has0) 1 else 0)) % MOD
  }
}
