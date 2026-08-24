// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

object Solution {
  def countTexts(pressedKeys: String): Int = {
    val mod = 1000000007
    val n = pressedKeys.length
    val dp = new Array[Int](n + 1)
    dp(0) = 1
    var i = 1
    while (i <= n) {
      dp(i) = dp(i - 1)
      val maxPress = if (pressedKeys.charAt(i - 1) == '7' || pressedKeys.charAt(i - 1) == '9') 4 else 3
      var j = 2
      var cont = true
      while (cont && j <= maxPress && j <= i) {
        if (pressedKeys.charAt(i - j) != pressedKeys.charAt(i - 1)) cont = false
        else {
          dp(i) = (dp(i) + dp(i - j)) % mod
          j += 1
        }
      }
      i += 1
    }
    dp(n)
  }
}
