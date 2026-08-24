// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

object Solution {
  def countDivisibleSubstrings(word: String): Int = {
    val vals = Array(1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9)
    var ans = 0
    val n = word.length
    var i = 0
    while (i < n) {
      var sum = 0
      var j = i
      while (j < n) {
        sum += vals(word.charAt(j) - 'a')
        if (sum % (j - i + 1) == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
