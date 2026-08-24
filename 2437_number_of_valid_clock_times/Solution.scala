// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

object Solution {
  def countTime(time: String): Int = {
    var ans = 0
    var h = 0
    while (h < 24) {
      var m = 0
      while (m < 60) {
        val h0 = ('0' + h / 10).toChar
        val h1 = ('0' + h % 10).toChar
        val m0 = ('0' + m / 10).toChar
        val m1 = ('0' + m % 10).toChar
        if ((time.charAt(0) == '?' || time.charAt(0) == h0) &&
            (time.charAt(1) == '?' || time.charAt(1) == h1) &&
            (time.charAt(3) == '?' || time.charAt(3) == m0) &&
            (time.charAt(4) == '?' || time.charAt(4) == m1)) {
          ans += 1
        }
        m += 1
      }
      h += 1
    }
    ans
  }
}
