// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

object Solution {
  def countBeautifulPairs(nums: Array[Int]): Int = {
    def firstDigit(x0: Int): Int = {
      var x = x0
      while (x >= 10) x /= 10
      x
    }
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var ans = 0
    val freq = Array.fill(10)(0)
    nums.foreach { x =>
      val last = x % 10
      var d = 1
      while (d <= 9) {
        if (freq(d) > 0 && gcd(d, last) == 1) ans += freq(d)
        d += 1
      }
      freq(firstDigit(x)) += 1
    }
    ans
  }
}
