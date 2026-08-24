// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

object Solution {
  def digitFrequencyScore(n: Int): Int = {
    var x = n
    var ans = 0
    while (x > 0) {
      ans += x % 10
      x /= 10
    }
    ans
  }
}
