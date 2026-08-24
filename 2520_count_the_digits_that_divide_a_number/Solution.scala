// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

object Solution {
  def countDigits(num: Int): Int = {
    var ans = 0
    var x = num
    while (x > 0) {
      val d = x % 10
      if (d != 0 && num % d == 0) ans += 1
      x /= 10
    }
    ans
  }
}
