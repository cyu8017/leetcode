// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

object Solution {
  def generateKey(num1: Int, num2: Int, num3: Int): Int = {
    var ans = 0
    var mul = 1
    var a = num1
    var b = num2
    var c = num3
    var t = 0
    while (t < 4) {
      val d = math.min(a % 10, math.min(b % 10, c % 10))
      ans += d * mul
      mul *= 10
      a /= 10; b /= 10; c /= 10
      t += 1
    }
    ans
  }
}
