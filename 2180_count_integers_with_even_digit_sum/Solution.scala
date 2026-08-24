// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

object Solution {
  def countEven(num: Int): Int = {
    var ans = 0
    var x = 1
    while (x <= num) {
      var s = 0
      var y = x
      while (y > 0) { s += y % 10; y /= 10 }
      if (s % 2 == 0) ans += 1
      x += 1
    }
    ans
  }
}
