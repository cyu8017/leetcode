// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

object Solution {
  def consecutiveNumbersSum(n: Int): Int = {
    var ans = 0
    var k = 1
    while (k.toLong * (k - 1) / 2 < n) {
      if ((n - k * (k - 1) / 2) % k == 0) ans += 1
      k += 1
    }
    ans
  }
}
