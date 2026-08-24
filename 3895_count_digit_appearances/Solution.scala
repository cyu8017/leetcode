// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

object Solution {
  def countDigitOccurrences(nums: Array[Int], digit: Int): Int = {
    var ans = 0
    nums.foreach { num =>
      var x = num
      while (x > 0) {
        if (x % 10 == digit) ans += 1
        x /= 10
      }
    }
    ans
  }
}
